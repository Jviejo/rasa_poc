# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.events import AllSlotsReset, EventType, SessionStarted, ActionExecuted
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    @staticmethod
    def fetch_slots(tracker: Tracker) -> List[EventType]:
        """Collect slots that contain the user's name and phone number."""

        slots = []

        for key in ("name", "phone_number"):
            value = tracker.get_slot(key)
            if value is not None:
                slots.append(SlotSet(key=key, value=value))

        return slots

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        # the session should begin with a `session_started` event
        events = [SessionStarted()]
        print("action start")
        # any slots that should be carried over should come after the
        # `session_started` event
        events.extend(self.fetch_slots(tracker))

        # an `action_listen` should be added at the end as a user message follows
        events.append(ActionExecuted("action_listen"))

        return events

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print(f'''hello {tracker.sender_id},slots=  {tracker.slots}, intent = {tracker.latest_message['intent']['name']},ultima_action= {tracker.latest_action_name}''')
        #print(f'current state = {tracker.current_state()}')
        #print(f'current_slot_values = {tracker.current_slot_values()}')
        #print(f'''get_latest_entity_values = {tracker.get_latest_entity_values('referencia')}''')

        dispatcher.utter_message(text="Hello World!111")

        return []

class ActionBorrar(Action):

    def name(self) -> Text:
        return "action_borrar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="vuelva a empezar")
        print(f'''cancelar {tracker.sender_id},slots=  {tracker.slots}, intent = {tracker.latest_message['intent']['name']},ultima_action= {tracker.latest_action_name}''')
        return [AllSlotsReset()]
