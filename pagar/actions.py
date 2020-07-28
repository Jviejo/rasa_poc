# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted
#from rasa.core.events import SlotSet
from rasa_sdk.forms import FormAction

class PagarForm(FormAction):

     def name(self) -> Text:
         return "pagar_form"

     @staticmethod
     def required_slots(tracker: Tracker) -> List[Text]:
        return ["referencia", "tarjeta", "cvv", "mmaa"]

     def submit(self, dispatcher: CollectingDispatcher, tracker:Tracker, domain: Dict[Text, Any])->List[Dict]:
         dispatcher.utter_template('utter_submit', tracker)
         return []

     def validate_cvv(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any] ) -> Dict[Text, Any]:
         if (int(value) > 99 and int(value)<1000):
             # validation succeeded, set the value of the "cvv" slot to value
             return {"cvv": value}
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
             return {"referencia": None}

     def validate_tarjeta(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any] ) -> Dict[Text, Any]:
         if  (len(value) == 16):
             return {"tarjeta": value}
         else:
	     dispatcher.utter_message(template="utter_wrong_referencia")	
             return {"tarjeta": None}

     def validate_mmaa(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any] ) -> Dict[Text, Any]:
         if  (len(value) == 4):
             return {"mmaa": value}
         else:
	     dispatcher.utter_message(template="utter_wrong_referencia")	
             return {"mmaa": None}
