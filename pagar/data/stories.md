## happy path 0
* init
  - utter_init

## happy path 1
* pagar
  - pagar_form
  - form{"name": "pagar_form"}
  - form{"name": null}
  - action_chat_restart
  - utter_init
## happy path 2
* pagar{"referencia":"111111111111", "tarjeta":"1234123412341234", "cvv":"123", "mmaa":"1121"}
  - pagar_form
  - form{"name": "pagar_form"}
  - form{"name": null}
  - action_chat_restart
  - utter_init
## happy path 3
* pagar{"referencia":"123456789012", "tarjeta":"9876987698769876", "cvv":"456"}
  - pagar_form
  - form{"name": "pagar_form"}
  - form{"name": null}
  - action_chat_restart
  - utter_init
## happy path 4
* pagar{"referencia":"234567890128"}
  - pagar_form
  - form{"name": "pagar_form"}
  - form{"name": null}
  - action_chat_restart
  - utter_init
