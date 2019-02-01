from typing import Dict, Text, Any, List, Union

from rasa_core_sdk import Action
from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet, AllSlotsReset
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT


class TravelForm(FormAction):

    def name(self):
        return "ride_booking_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["TypeOfVehicle", "start_location", "end_location", "PaymentType", "preferences"]

    def slot_mappings(self):
        return {"TypeOfVehicle": [self.from_entity(entity="TypeOfVehicle",
                                                intent=["request_ride","thankyou"]),
                                self.from_text(intent="request_ride")],

                "start_location": [self.from_entity(entity="start_location",
                                                intent=["inform",
                                                        "request_ride"]),
                               self.from_entity(entity="location"),
                               self.from_text(intent="inform")],

                "end_location": [self.from_entity(entity="end_location",
                                                intent=["inform","request_ride"]),
                               self.from_entity(entity="location"),
                               self.from_text(intent="inform")],

                "preferences": [self.from_intent(intent='deny',
                                                 value="No additional "
                                                       "preference"),
                             self.from_text()],

                "PaymentType": [self.from_entity(entity="PaymentType"),
                                self.from_text()]}

    @staticmethod
    def TypeOfVehicle_db():
        return ["Car", "Taxi", "Mini-car", "Bike", "Auto-rikshaw", "Auto", "Rikshaw", "Tempo", "Truck", "Bus Ticket", "Ship", "Boat", "Cruise", "Train Ticket", "Helicoptor", "Flight Ticket"]


    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:

        slot_values = self.extract_other_slots(dispatcher, tracker, domain)


        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0}"
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))

        for slot, value in slot_values.items():
            if slot == "TypeOfVehicle":
                if value not in self.TypeOfVehicle_db():
                    dispatcher.utter_template('utter_wrong_TypeOfVehicle', tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None

        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        # utter submit template
        dispatcher.utter_template('utter_submit', tracker)
        return []


class ActionSlotReset(Action):
    def name(self):
        return "action_slot_reset"
    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]



