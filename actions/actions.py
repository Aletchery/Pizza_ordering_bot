from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

ALLOWED_PIZZA_SIZES = ["malá", "veľká", "stredná", "mala", "velka", "stredna",]
ALLOWED_PIZZA_TYPES = ["salámová", "šunková", "syrová", "hawaii"]

class ValidateSimplePizzaForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_simple_pizza_form"

    def validate_pizza_size(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `pizza_size` value."""

        if slot_value.lower() not in ALLOWED_PIZZA_SIZES:
            dispatcher.utter_message(text=f"Takú veľkosť nemáme. Dostupné veľkosti sú malá, stredná, veľká")
            return {"pizza_size": None}
        dispatcher.utter_message(text=f"OK! chcete veľkosť: {slot_value}")
        return {"pizza_size": slot_value}

    def validate_pizza_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `pizza_type` value."""

        if slot_value not in ALLOWED_PIZZA_TYPES:
            dispatcher.utter_message(text=f"Takú pizzu nemáme! Máme iba {'/'.join(ALLOWED_PIZZA_TYPES)}.")
            return {"pizza_type": None}
        dispatcher.utter_message(text=f"OK! Chcete {slot_value} pizza.")
        return {"pizza_type": slot_value}

    def validate_delivery_phone_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `pizza_size` value."""
        if not slot_value.isdigit() or len(slot_value) != 10: 
            dispatcher.utter_message(text=f"Chybné číslo! Zadajte číslo v tvare 09xxxxxxxx")
            return {"delivery_phone_number": None}
        dispatcher.utter_message(text=f"OK! Vaše čislo je: {slot_value}")
        return {"delivery_phone_number": slot_value}


    def validate_delivery_adress(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        dispatcher.utter_message(text=f"OK! Tvoja adresa je: {slot_value}")
        return {"delivery_adress": slot_value}
    
   

   

