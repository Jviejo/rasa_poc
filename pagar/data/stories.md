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

## deviation 1
* pagar
  - pagar_form
  - form{"name":"pagar_form"}
* cancelar
  - utter_continuar
* confirmar
  - pagar_form
  - form{"name":null}
  - utter_slots_values

## deviation 2
* pagar
  - pagar_form
  - form{"name":"pagar_form"}
* cancelar
  - utter_continuar
* abandonar
  - utter_abandonar

## deviation 3
* pagar
  - pagar_form
  - form{"name":"pagar_form"}
  - slot{"referencia":"123456789012"}
* cancelar
  - utter_continuar
* abandonar
  - utter_abandonar
