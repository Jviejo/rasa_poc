## happy path 0
* init
  - utter_init

## happy path 1
* pagar
  - pagar_form
  - form{"name": "pagar_form"}
  - form{"name": null}
  - utter_slots_values

## happy path 2
* pagar{"referencia":"012345678912"}
  - slot{"referencia":"012345678912"}
  - pagar_form
  - form{"name":"pagar_form"}
  - form{"name": null}
  - utter_slots_values

## happy path 2.1
* pagar{"referencia": "012345678912", "tarjeta":"1234123412341234", "cvv":"123", "mmaa":"1223"}
  - slot{"referencia": "012345678912"}
  - slot{"tarjeta": "1234123412341234"}
  - slot{"cvv":"123"}
  - slot{"mmaa":"1223"}
  - pagar_form
  - form{"name":"pagar_form"}
  - form{"name": null}
  - utter_slots_values
  

## deviation 1
* pagar
  - pagar_form
  - form{"name":"pagar_form"}
* cancelar
  - utter_confirmar_cancelar
* negar
  - pagar_form
  - form{"name": null}
  - utter_slots_values

## deviation 1.1
* pagar
  - pagar_form
  - form{"name": "pagar_form"}
* cancelar
  - utter_confirmar_cancelar
* afirmar
  - action_deactivate_form
  - form{"name": null}
  - utter_abandonar

## deviation 2
* pagar
  - pagar_form
  - form{"name":"pagar_form"}
  - slot{"referencia": "123456789012"}
* cancelar
  - utter_confirmar_cancelar
* negar
  - pagar_form
  - form{"name": null}
  - utter_slots_values

## deviation 2.1
* pagar
  - pagar_form
  - form{"name": "pagar_form"}
  - slot{"referencia":"123456789012"}
* cancelar
  - utter_confirmar_cancelar
* afirmar
  - action_deactivate_form
  - form{"name": null}
  - utter_abandonar

## deviation 3
* pagar
  - pagar_form
  - form{"name":"pagar_form"}
  - slot{"referencia": "123456789012"}
  - slot{"tarjeta": "1234567890123456"}
* cancelar
  - utter_confirmar_cancelar
* negar
  - pagar_form
  - form{"name": null}
  - utter_slots_values

## deviation 3.1
* pagar
  - pagar_form
  - form{"name": "pagar_form"}
  - slot{"referencia": "123456789012"}
  - slot{"tarjeta": "1234567890123456"}
* cancelar
  - utter_confirmar_cancelar
* afirmar
  - action_deactivate_form
  - form{"name": null}
  - utter_abandonar

