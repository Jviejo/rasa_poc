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
  - slot{"requested_slot":"referencia"}
* cancelar
  - utter_confirmar_cancelar
* negar
  - pagar_form
  - form{"name": null}
  - utter_slots_values

## deviation 2
* pagar
  - pagar_form
  - form{"name": "pagar_form"}
* cancelar
  - utter_confirmar_cancelar
* afirmar
  - action_deactivate_form
  - form{"name": null}
  - utter_abandonar

