while True:
    n=int(input('Qual Tabuada? '))
    print('-'*30)
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
    continuar =  str(input('Deseja Continuar [S/N]: '))
    if continuar in 'Nn':
        break