
## happy path 1
* pagar
  - pagar_form
  - form{"name": "pagar_form"}
  - form{"name": null}
  - action_chat_restart

## happy path 2
* pagar
  - pagar_form
  - form{"name": "pagar_form"}
  - slot{"referencia": "123456789012"}
  - form{"name": null}
  - action_chat_restart

## happy path 3
* pagar
  - pagar_form
  - form{"name": "pagar_form"}
  - slot{"referencia": "123456789012"}
  - slot{"tarjeta": "1234123412341234"}
  - form{"name": null}
  - action_chat_restart

## happy path 4
* pagar
  - pagar_form
  - form{"name": "pagar_form"}
  - slot{"referencia": "123456789012"}
  - slot{"tarjeta": "1234123412341234"}
  - slot{"cvv": "123"}
  - form{"name": null}
  - action_chat_restart

## happy path 5
* pagar
  - pagar_form
  - form{"name": "pagar_form"}
  - slot{"referencia": "123456789012"}
  - slot{"tarjeta": "1234123412341234"}
  - slot{"cvv": "123"}
  - slot{"mmaa": "1121"}
  - form{"name": null}
  - action_chat_restart


