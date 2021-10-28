diadasemana=str(input())
dia=int(input())
dias=['domingo','segunda','terca','quarta','quinta','sexta','sabado']
hoje = dias.index(diadasemana)
entrega =  (hoje + dia)-7
if dia == 0:
    print('chega hoje!')
else:
    print(f'sera entregue {dias[entrega]}')