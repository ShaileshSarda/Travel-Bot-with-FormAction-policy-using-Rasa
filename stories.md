## story 001
* greet
    - utter_greet
* request_ride
    - ride_booking_form
    - form{"name": "ride_booking_form"}
    - form{"name": null}
    - utter_slots_values
* deny
    - utter_not_confirm_booking
* thankyou
    - utter_noworries
    - action_slot_reset
    - reset_slots

## story 002
* greet
    - utter_greet
* request_ride
    - ride_booking_form
    - form{"name": "ride_booking_form"}
    - form{"name": null}
    - utter_slots_values
* affirm
    - utter_confirm_booking
* thankyou
    - utter_noworries
    - action_slot_reset
    - reset_slots

## story 003
* greet
    - utter_greet
* request_ride
    - ride_booking_form
    - form{"name": "ride_booking_form"}
* chitchat
    - utter_chitchat
    - ride_booking_form
    - form{"name": null}
    - utter_slots_values
* deny
    - utter_not_confirm_booking
* thankyou
    - utter_noworries
    - action_slot_reset
    - reset_slots


## story 004
* greet
    - utter_greet
* request_ride
    - ride_booking_form
    - form{"name": "ride_booking_form"}
* chitchat
    - utter_chitchat
    - ride_booking_form
    - form{"name": null}
    - utter_slots_values
* affirm
    - utter_confirm_booking
* thankyou
    - utter_noworries
    - action_slot_reset
    - reset_slots


## story 005
* greet
    - utter_greet
* request_ride
    - ride_booking_form
    - form{"name": "ride_booking_form"}
* chitchat
    - utter_chitchat
    - ride_booking_form
* chitchat
    - utter_chitchat
    - ride_booking_form
* chitchat
    - utter_chitchat
    - ride_booking_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries
    - action_slot_reset
    - reset_slots


## story 006
* greet
    - utter_greet
* request_ride
    - ride_booking_form
    - form{"name": "ride_booking_form"}
* stop
    - utter_ask_continue
* affirm
    - ride_booking_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries
    - action_slot_reset
    - reset_slots

## story 007
* greet
    - utter_greet
* request_ride
    - ride_booking_form
    - form{"name": "ride_booking_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}

## story 008
* request_ride
    - ride_booking_form
    - form{"name": "ride_booking_form"}
* chitchat
    - utter_chitchat
    - ride_booking_form
* stop
    - utter_ask_continue
* affirm
    - ride_booking_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries
    - action_slot_reset
    - reset_slots


## story 009
* greet
    - utter_greet
* request_ride
    - ride_booking_form
    - form{"name": "ride_booking_form"}
* stop
    - utter_ask_continue
* affirm
    - ride_booking_form
* chitchat
    - utter_chitchat
    - ride_booking_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries
    - action_slot_reset
    - reset_slots


## story 010
* greet
    - utter_greet
* request_ride
    - ride_booking_form
    - form{"name": "ride_booking_form"}
* chitchat
    - utter_chitchat
    - ride_booking_form
* stop
    - utter_ask_continue
* affirm
    - ride_booking_form
* chitchat
    - utter_chitchat
    - ride_booking_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries
    - action_slot_reset
    - reset_slots


## story 011
* greet
    - utter_greet
* request_ride
    - ride_booking_form
    - form{"name": "ride_booking_form"}
* chitchat
    - utter_chitchat
    - ride_booking_form
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - action_slot_reset
    - reset_slots


## story 012
* greet
    - utter_greet
* request_ride
    - ride_booking_form
    - form{"name": "ride_booking_form"}
    - slot{"requested_slot": "TypeOfVehicle"}
* chitchat
    - utter_chitchat  <!-- ride_booking_form was predicted by FormPolicy and rejected, other policy predicted utter_chitchat -->
    - ride_booking_form
    - slot{"requested_slot": "TypeOfVehicle"}
* form: inform{"TypeOfVehicle": "Car"}
    - slot{"TypeOfVehicle": "Car"}
    - form: ride_booking_form
    - slot{"TypeOfVehicle": "Car"}
    - slot{"requested_slot": "start_location"}
* form: inform{"start_location": "Pune Station"}
    - form: ride_booking_form
    - slot{"start_location": "Pune Station"}
    - slot{"requested_slot": "end_location"}
* chitchat
    - utter_chitchat
    - ride_booking_form
    - slot{"requested_slot": "end_location"}
* stop
    - utter_ask_continue
* affirm
    - ride_booking_form  <!-- FormPolicy predicted FormValidation(False), other policy predicted ride_booking_form -->
    - slot{"requested_slot": "end_location"}
* form: affirm
    - form: ride_booking_form
    - slot{"requested_slot": "preferences"}
* form: inform
    - form: ride_booking_form
    - slot{"end_location": "/inform"}
    - slot{"requested_slot": "preferences"}
* form: inform
    - form: ride_booking_form
    - slot{"preferences": "/inform"}
    - slot{"requested_slot": "PaymentType"}
* form: inform{"PaymentType": "Online Mode"}
    - slot{"PaymentType": "great"}
    - form: ride_booking_form
    - slot{"PaymentType": "Online Mode"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slots_values
* form: inform{"confirm_booking": "yes"}
    - slot{"confirm_booking": "yes"}
    - form: ride_booking_form
    - slot{"confirm_booking": "yes"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slots_values
* thankyou
    - utter_ask_continue
* thankyou
    - utter_noworries
    - action_slot_reset
    - reset_slots


## story 013
* greet
    - utter_greet
* request_ride
    - ride_booking_form
    - form{"name": "ride_booking_form"}
    - slot{"requested_slot": "TypeOfVehicle"}
* chitchat
    - utter_chitchat  <!-- ride_booking_form was predicted by FormPolicy and rejected, other policy predicted utter_chitchat -->
    - ride_booking_form
    - slot{"requested_slot": "TypeOfVehicle"}
* form: inform{"TypeOfVehicle": "Taxi"}
    - slot{"TypeOfVehicle": "Taxi"}
    - form: ride_booking_form
    - slot{"TypeOfVehicle": "Taxi"}
    - slot{"requested_slot": "start_location"}
* form: inform{"location": "Pune station"}
    - form: ride_booking_form
    - slot{"start_location": "Pune Station"}
    - slot{"requested_slot": "end_location"}

* form: inform{"location":"Mumbai"}
    - form: ride_booking_form
    - slot{"end_location": "Mumbai"}
    - slot{"requested_slot": "end_location"}
* stop
    - utter_ask_continue
* affirm
    - ride_booking_form  <!-- FormPolicy predicted FormValidation(False), other policy predicted ride_booking_form -->
    - slot{"requested_slot": "end_location"}
* form: affirm
    - form: ride_booking_form
    - slot{"requested_slot": "preferences"}
* form: affirm
    - form: ride_booking_form
    - slot{"requested_slot": "preferences"}
* form: inform
    - form: ride_booking_form
    - slot{"end_location": "/inform"}
    - slot{"requested_slot": "preferences"}
* form: inform
    - form: ride_booking_form
    - slot{"preferences": "/inform"}
    - slot{"requested_slot": "PaymentType"}
* form: inform{"PaymentType": "Cash"}
    - slot{"PaymentType": "Cash"}
    - form: ride_booking_form
    - slot{"PaymentType": "Cash"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slots_values
* form: inform{"confirm_booking": "yes"}
    - slot{"confirm_booking": "yes"}
    - form: ride_booking_form
    - slot{"confirm_booking": "yes"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slots_values
* deny
    - utter_not_confirm_booking
* thankyou
    - utter_noworries
    - action_slot_reset
    - reset_slots

## story 014
* greet
    - utter_greet
* request_ride
    - ride_booking_form
    - form{"name": "ride_booking_form"}
    - form{"name": null}
    - utter_slots_values
* affirm
    - utter_confirm_booking
* thankyou
    - utter_noworries
    - action_slot_reset
    - reset_slots

## story 015
* greet
    - utter_greet
* request_ride
    - ride_booking_form
    - form{"name": "ride_booking_form"}
* affirm
    - utter_confirm_booking
* thankyou
    - utter_noworries
    - action_slot_reset
    - reset_slots

## story 016
* greet
    - utter_greet
* request_ride
    - ride_booking_form
    - form{"name": "ride_booking_form"}
* thankyou
    - utter_noworries
    - action_slot_reset
    - reset_slots

## story 017
* greet
    - utter_greet
* request_ride
    - ride_booking_form
    - form{"name": "ride_booking_form"}
    - ride_booking_form
* stop
    - utter_ask_continue
* affirm
    - ride_booking_form
* request_ride
    - ride_booking_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries
    - action_slot_reset
    - reset_slots

