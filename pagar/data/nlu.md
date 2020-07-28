## intent:pagar
- quiero pagar 
- quiero pagar recibo
- pagar
- pagar recibo
- pagar recibo [0002415611](referencia)
- pagar recibo [0012345678](referencia)
- pagar recibo [9876554433](referencia)
- pagar recibo [0009789697](referencia) con tarjeta [7169 9033 4370 1795](tarjeta)
- pagar recibo [0002476789](referencia) con tarjeta [7169 9033 4370 1795](tarjeta)
- pagar recibo [0002415567](referencia) con tarjeta [7169 9033 4370 1795](tarjeta)
- pagar recibo [9876554433](referencia) con tarjeta [7169 9033 4370 1795](tarjeta)
- pagar recibo [9876554433](referencia) con tarjeta [7169 9033 4370 1795](tarjeta) con código [739](cvv)
- pagar recibo [9876554433](referencia) con tarjeta [7169 9033 4370 1795](tarjeta) con código [404](cvv)
- pagar recibo [9876554433](referencia) con tarjeta [7169 9033 4370 1795](tarjeta) con código [865](cvv) 
- pagar recibo [9876554433](referencia) con tarjeta [7169 9033 4370 1795](tarjeta) con código [739](cvv) y caducidad [1127](mmaa)
- pagar recibo [9876554433](referencia) con tarjeta [7169 9033 4370 1795](tarjeta) con código [404](cvv) y caducidad [0120](mmaa)
- pagar recibo [9876554433](referencia) con tarjeta [7169 9033 4370 1795](tarjeta) con código [865](cvv) y caducidad [1222](mmaa)

## intent:inform
- [0012345678](referencia)
- [0001234567](referencia)
- [7169 9033 4370 1795](tarjeta)
- [8765 4772 3335 2966](tarjeta)
- [185](cvv)
- [329](cvv)
- [127](cvv)
- [193](cvv)
- [1100](mmaa)
- [0422](mmaa)
- [0945](mmaa)
- [1221](mmaa)

## intent:cancelar
- cancelo
- quiero cancelar
- cancela

## lookup:mmaa
- 0120
- 0220
- 0321
- 0422
- 0523
- 0626
- 0720

## lookup:cvv
- 949
- 533
- 640
- 444
- 867
- 866

## lookup:referencia

- 0002415611
- 0007616398
- 0002840971
- 0013752379
- 0015451613
- 0008134842
- 0017952591
- 0014768005
- 0012460715
- 0018293470
- 0018497996
- 0013165722
- 0012403796
- 0007898072
- 0014727904
- 0012345678

## lookup:tarjeta
- 6894 5790 1276 7429
- 1591 5198 1009 3527
- 5807 3092 3097 1633
- 6593 6294 7368 2126
- 7181 8074 8031 5904

## regex:referencia
- [0-9]{10}

## regex:cvv
- [0-9]{3}

## regex:mmaa
- [0-9]{4}
