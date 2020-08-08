# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

import logging
from rasa_sdk.interfaces import Action, ActionExecutionRejection

from typing import Any, Text, Dict, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset, EventType
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet
from rasa.core.events import Event
from rasa.core.domain import Domain
from rasa.core.channels import OutputChannel
from rasa.core.nlg import NaturalLanguageGenerator
from rasa_sdk.events import FollowupAction
from rasa_sdk.events import Restarted

#This slot is used to store information needed to do the form handling
REQUESTED_SLOT= "requested_slot"
logger = logging.getLogger(__name__)

class ActionRestarted(Action):
   def name(self) -> Text:
      return "action_chat_restart"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text= "Action_Restart: Entre nuevo comando")
        return [Restarted()]

class PagarForm(FormAction):

     def name(self) -> Text:
         return "pagar_form"
     
     async def validate(
          self,
          dispatcher: "CollectingDispatcher",
          tracker: "Tracker",
          domain: Dict[Text, Any],
          ) -> List[EventType]:
        """Extract and validate value of requested slot.

        If nothing was extracted reject execution of the form action.
        Subclass this method to add custom validation and rejection logic
        """

        # extract other slots that were not requested
        # but set by corresponding entity or trigger intent mapping
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        # extract requested slot
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))
        logger.debug(f"Validating extracted slots: {slot_values}")
        return await self.validate_slots(slot_values, dispatcher, tracker, domain)


     def request_next_slot(self, dispatcher:"CollectingDispatcher", tracker: "Tracker", domain: Dict[Text, Any],  )->Optional[List[EventType]]:
       
        last_intent= tracker.latest_message.get('intent')['name']
        if last_intent == 'confirmar_cancelar':
          print("Se confirma la cancelación")
          return self.deactivate()        
        
        for slot in self.required_slots(tracker): 
            if self._should_request_slot(tracker, slot):
                print(f"Request next slot '{slot}'")
                #logger.debug(f"Request next slot '{slot}'")
                message= tracker.latest_message.get('text')
                intent= tracker.latest_message.get('intent')['name']
                if intent == "cancelar":
                   return  self.deactivate()

                dispatcher.utter_message(template=f"utter_ask_{slot}", **tracker.slots)
                return [SlotSet(REQUESTED_SLOT, slot)]
        return None
        
     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
      
       return {
           "referencia": [self.from_entity(entity="referencia", intent=["inform_referencia", "pagar"])],
           "tarjeta": [self.from_entity(entity="tarjeta", intent=["inform_tarjeta", "pagar"])],
           "cvv": [self.from_entity(entity="cvv", intent=["inform_cvv", "pagar"])],
           "mmaa": [self.from_entity(entity="mmaa", intent=["inform_mmaa", "pagar"])],
           
       }

     @staticmethod
     def required_slots(tracker: Tracker) -> List[Text]:  
        return ["referencia", "tarjeta", "cvv", "mmaa"]

     def submit(self, dispatcher: CollectingDispatcher, tracker:Tracker, domain: Dict[Text, Any])->List[Dict]:
         slot_values= tracker.current_slot_values()
         
         if slot_values["referencia"] and slot_values["tarjeta"] and slot_values["cvv"] and slot_values["mmaa"]:
              message= "Submit: Recibo pagado con referencia {}, tarjeta {}, código {} y fecha de caducidad {}".format(slot_values["referencia"], slot_values["tarjeta"], slot_values["cvv"], slot_values["mmaa"])
         else:
              message= "Submit: ¿Está seguro que abandona la operación?"

         dispatcher.utter_message(text=message) 
         return [AllSlotsReset()]

         
     def validate_cvv(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any] ) -> Dict[Text, Any]:
         print("Validando CVV ...")
         if (int(value) > 99 and int(value)<1000):
             # validation succeeded, set the value of the "cvv" slot to value
             #slot_values= self.extract_other_slots(dispatcher, tracker, domain)
             slot_values= tracker.current_slot_values()
             print(slot_values)
             #if ("referencia" in slot_values.items() and "tarjeta" in slot_values.items()):
             if slot_values["requested_slot"] == 'cvv' or slot_values["requested_slot"] == None:
                return {"cvv": value}
             else:
                dispatcher.utter_message(template="utter_wrong")
                print("valor actual de CVV: ", {slot_values["cvv"]})
                return {"cvv": slot_values["cvv"]}
         else:
             dispatcher.utter_message(template="utter_wrong")
             # validation failed, set this slot to None, meaning the
             # user will be asked for the slot again
             return {"cvv": None}

     def validate_referencia(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any] ) -> Dict[Text, Any]:
                      
         slot_values= tracker.current_slot_values()
         print("Validando referencia ...")

         if  (len(value) == 12):
             print(slot_values)
             if slot_values["requested_slot"] == "referencia" or slot_values["requested_slot"] == None:
                 return {"referencia": value, "cvv": None, "mmaa": None}
             else:
                 dispatcher.utter_message(template="utter_wrong")
                 return {"referencia": slot_values["referencia"], "cvv": None, "mmaa": None}
         else:
             if  slot_values["requested_slot"] == None:
                dispatcher.utter_message(text="Parámetro incorrecto en la secuencia")
             else:
                dispatcher.utter_message(template="utter_wrong")
             return {"referencia": slot_values["referencia"], "tarjeta": slot_values["tarjeta"], "cvv": slot_values["cvv"], "mmaa": slot_values["mmaa"]}

     def validate_tarjeta(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any] ) -> Dict[Text, Any]:
         if  (len(value) == 16):
             slot_values= tracker.current_slot_values()
             print("Validando Tarjeta ...")
             print(slot_values)
             if  slot_values["requested_slot"] == "tarjeta" or slot_values["requested_slot"] == None:
                 return {"tarjeta": value, "cvv": None, "mmaa": None}
             else:
                 dispatcher.utter_message(template="utter_wrong")
                 return {"tarjeta": slot_values["tarjeta"], "cvv": None, "mmaa": None}
         else:
             dispatcher.utter_message(template="utter_wrong")
             return {"tarjeta": None, "cvv": None, "mmaa": None}

     @staticmethod
     def meses_db() -> List[Text]:
         return ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
     
     @staticmethod
     def años_db() -> List[Text]:
        return ["20", "21", "22", "23", "24", "25"]

     def validate_mmaa(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any] ) -> Dict[Text, Any]:
            
         print("Validando fecha ...")
         if  (len(value) == 4 and value[0:2] in self.meses_db() and value[2:4] in self.años_db()):
             slot_values= tracker.current_slot_values()
             print(slot_values)
             if slot_values["requested_slot"]=="mmaa" or slot_values["requested_slot"] == None:
               print("Fecha aceptada")
               return {"mmaa": value}
             else: 
               dispatcher.utter_message(template="utter_wrong")
               return {"mmaa": slot_values["mmaa"]}
         else:
              dispatcher.utter_message(template="utter_wrong")
              return {"mmaa": None}
