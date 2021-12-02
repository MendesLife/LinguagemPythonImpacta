primeiros_valores = input()
lista_valores = list(map(int, primeiros_valores.split()))
i=0
while True:
    entrada = input().split()
    if entrada[0] == "adicionar":
        lista_valores.append(int(entrada[1]))
    elif entrada[0] == "remover":
        if (int(entrada[1]) in lista_valores):
            lista_valores.remove(int(entrada[1]))
        else:
            print(f"código {entrada[1]} não encontrado")
    if entrada[0] == 'exibir':
        lista_valores.sort()
        for c in lista_valores:
            print(f'{lista_valores[i]}',end=' ')
            i+=1
        print('')
        i=0
    if entrada[0] == 'encerrar':
        lista_valores.sort()
        for c in lista_valores:
            print(f'{lista_valores[i]}',end=' ')
            i+=1
        break