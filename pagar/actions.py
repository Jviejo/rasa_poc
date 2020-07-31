# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted
#from rasa.core.events import SlotSet
from rasa_sdk.forms import FormAction

class PagarForm(FormAction):

     def name(self) -> Text:
         return "pagar_form"
     
     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
       
        return  {
           
           
           "referencia": [self.from_entity(entity="referencia", intent=["inform_referencia","pagar"]), self.from_text()],
           "tarjeta": [self.from_entity(entity="tarjeta", intent=["inform_tarjeta", "pagar"]), self.from_text()],
           "cvv": [self.from_entity(entity="cvv", intent=["inform_cvv","pagar"]), self.from_text()],
           "mmaa": [self.from_entity(entity="mmaa", intent=["inform_mmaa","pagar"]), self.from_text()]

           #"referencia": [self.from_entity(entity="referencia", intent=["inform_referencia"])],
           #"tarjeta": [self.from_entity(entity="tarjeta", intent=["inform_tarjeta"])],
           #"cvv": [self.from_entity(entity="cvv", intent=["inform_cvv"])],
           #"mmaa": [self.from_entity(entity="mmaa", intent=["inform_mmaa"])]
       }

     @staticmethod
     def required_slots(tracker: Tracker) -> List[Text]:
        return ["referencia", "tarjeta", "cvv", "mmaa"]

     def submit(self, dispatcher: CollectingDispatcher, tracker:Tracker, domain: Dict[Text, Any])->List[Dict]:
         dispatcher.utter_template('utter_submit', tracker)
         return []

     def validate_cvv(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any] ) -> Dict[Text, Any]:
         if (int(value) > 99 and int(value)<1000):
             # validation succeeded, set the value of the "cvv" slot to value
             print("Codigo cvv validado")

             #slot_values= self.extract_other_slots(dispatcher, tracker, domain)
             slot_values= tracker.current_slot_values()
             #if ("referencia" in slot_values.items() and "tarjeta" in slot_values.items()):
             if slot_values["requested_slot"] == 'cvv':
                return {"cvv": value}
             else:
                return {"cvv": None}
         else:
             dispatcher.utter_message(template="utter_wrong_cvv")
             # validation failed, set this slot to None, meaning the
             # user will be asked for the slot again
             return {"cvv": None}

     def validate_referencia(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any] ) -> Dict[Text, Any]:
         if  (len(value) == 12):
             return {"referencia": value}
         else:
             dispatcher.utter_message(template="utter_wrong_referencia")
           
             slot_values= self.extract_other_slots(dispatcher, tracker, domain)
             #for slot, value in slot_values.items():
                  #if (slot == "cvv" or slot == "mmaa"):
                  #  print(slot)
                   # SlotSet(slot_values[slot], None)

             return {"referencia": None}

     def validate_tarjeta(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any] ) -> Dict[Text, Any]:
         if  (len(value) == 16):
             slot_values= tracker.current_slot_values()
             if  slot_values["requested_slot"] == "tarjeta":
                 return {"tarjeta": value}
             else:
                 return {"tarjeta": None}
         else:
             dispatcher.utter_message(template="utter_wrong_tarjeta")
             return {"tarjeta": None}

     @staticmethod
     def meses_db() -> List[Text]:
         return ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
     
     @staticmethod
     def años_db() -> List[Text]:
        return ["20", "21", "22", "23", "24", "25"]

     def validate_mmaa(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any] ) -> Dict[Text, Any]:
         if  (len(value) == 4 and value[0:2] in self.meses_db() and value[2:4] in self.años_db()):
             slot_values= tracker.current_slot_values()
             if slot_values["requested_slot"]=="mmaa":
               return {"mmaa": value}
             else: 
               return {"mmaa": None}
         else:
              dispatcher.utter_message(template="utter_wrong_mmaa")
              return {"mmaa": None}
