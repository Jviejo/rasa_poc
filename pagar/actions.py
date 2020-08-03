# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.forms import FormAction

class PagarForm(FormAction):

     def name(self) -> Text:
         return "pagar_form"
     
     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

       return {
           "referencia": [self.from_entity(entity="referencia", intent=["inform_referencia","pagar"])],
           "tarjeta": [self.from_entity(entity="tarjeta", intent=["inform_tarjeta", "pagar"])],
           "cvv": [self.from_entity(entity="cvv", intent=["inform_cvv","pagar"])],
           "mmaa": [self.from_entity(entity="mmaa", intent=["inform_mmaa","pagar"])],
       }

     @staticmethod
     def required_slots(tracker: Tracker) -> List[Text]:
        return ["referencia", "tarjeta", "cvv", "mmaa"]

     def submit(self, dispatcher: CollectingDispatcher, tracker:Tracker, domain: Dict[Text, Any])->List[Dict]:
         print ("Enviando datos del formulario ....") 
         slot_values= tracker.current_slot_values()
         print(slot_values)       
         #dispatcher.utter_template('utter_submit', tracker)
         message= "Recibo pagado con referencia {}, tarjeta {}, código {} y fecha de caducidad {}".format(slot_values["referencia"], slot_values["tarjeta"], slot_values["cvv"], slot_values["mmaa"])
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
                return {"cvv": slot_values["cvv"]}
         else:
             dispatcher.utter_message(template="utter_wrong")
             # validation failed, set this slot to None, meaning the
             # user will be asked for the slot again
             return {"cvv": None}

     def validate_referencia(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any] ) -> Dict[Text, Any]:

         if  (len(value) == 12):
             slot_values= tracker.current_slot_values()
             print("Validando referencia ...")
             print(slot_values)
             if slot_values["requested_slot"] == "referencia" or slot_values["requested_slot"] == None:
                 return {"referencia": value}
             else:
                 dispatcher.utter_message(template="utter_wrong")
                 return {"referencia": slot_values["referencia"]}
         else:
             dispatcher.utter_message(template="utter_wrong")
           
             return {"referencia": None}

     def validate_tarjeta(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any] ) -> Dict[Text, Any]:
         if  (len(value) == 16):
             slot_values= tracker.current_slot_values()
             print("Validando Tarjeta ...")
             print(slot_values)
             if  slot_values["requested_slot"] == "tarjeta" or slot_values["requested_slot"] == None:
                 return {"tarjeta": value}
             else:
                 dispatcher.utter_message(template="utter_wrong")
                 return {"tarjeta": slot_values["tarjeta"]}
         else:
             dispatcher.utter_message(template="utter_wrong")
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
             print("Validando fecha ...")
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
