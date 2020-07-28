## activate pagar form
* pagar
  - pagar_form
  - form{"name": "pagar_form"}
* form: inform_referencia{"referencia": "012345678912"}   
  - slot{"referencia": "012345678912"}
  - form: pagar_form
  - slot{"referencia": "012345678912"}
* form: inform_tarjeta{"tarjeta": "1234567812345678"}   
  - slot{"tarjeta": "1234567812345678"}
  - form: pagar_form
  - slot{"tarjeta": "1234567812345678"}
* form: inform_cvv{"cvv": "123"}   
  - slot{"cvv": "123"}
  - form: pagar_form
  - slot{"cvv": "123"}
* form: inform_mmaa{"mmaa": "1223"}   
  - slot{"mmaa": "1223"}
  - form: pagar_form
  - slot{"mmaa": "1223"}


