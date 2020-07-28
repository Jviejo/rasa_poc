## intent:pagar
- quiero pagar 
- quiero pagar recibo
- pagar
- pagar recibo
- pagar recibo [000241561112](referencia)
- pagar recibo [001234567823](referencia)
- pagar recibo [987655443334](referencia)
- pagar recibo [000978969756](referencia) con tarjeta [7169903343701795](tarjeta)
- pagar recibo [000247678965](referencia) con tarjeta [7169903343701795](tarjeta)
- pagar recibo [000241556743](referencia) con tarjeta [7169903343701795](tarjeta)
- pagar recibo [987655443376](referencia) con tarjeta [7169903343701795](tarjeta)
- pagar recibo [987655443355](referencia) con tarjeta [7169903343701795](tarjeta) con código [739](cvv)
- pagar recibo [987655443343](referencia) con tarjeta [7169903343701795](tarjeta) con código [404](cvv)
- pagar recibo [987655443310](referencia) con tarjeta [7169903343701795](tarjeta) con código [865](cvv) 
- pagar recibo [987655443300](referencia) con tarjeta [7169903343701795](tarjeta) con código [739](cvv) y caducidad [1127](mmaa)
- pagar recibo [987655443309](referencia) con tarjeta [7169903343701795](tarjeta) con código [404](cvv) y caducidad [0120](mmaa)
- pagar recibo [987655443309](referencia) con tarjeta [7169903343701795](tarjeta) con código [865](cvv) y caducidad [1222](mmaa)

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

- 000241561198
- 000761639878
- 000284097165
- 001375237943
- 001545161322
- 000813484212
- 001795259134
- 001476800556
- 001246071577
- 001829347065
- 001849799643
- 001316572221
- 001240379612
- 000789807299
- 001472790498
- 001234567876

## lookup:tarjeta
- 6894579012767429
- 1591519810093527
- 5807309230971633
- 6593629473682126
- 7181807480315904

## regex:referencia
- [0-9]{12}

## regex:cvv
- [0-9]{3}

## regex:mmaa
- [0-9]{4}

## regex:tarjeta
- [0-9]{16}
