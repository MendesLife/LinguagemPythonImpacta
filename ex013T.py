inciais=input().split()
cdprodutos=[]
i=0
a=0
for l in inciais:
    inciais[a]=int(inciais[a])
    cdprodutos.append(inciais[a])
    a+=1
while True:
    adicionar = input().split()
    if adicionar[0] == 'adicionar':
        cdprodutos.append(int(adicionar[1]))
    if adicionar[0] == 'remover':
        if (int(adicionar[1]) in cdprodutos):
            cdprodutos.remove(int(adicionar[1]))
        else:
            print(f'código {adicionar[1]} não encontrado')
    if adicionar[0] == 'exibir':
        cdprodutos.sort()
        for c in cdprodutos:
            print(f'{cdprodutos[i]}',end=' ')
            i+=1
        print('')
        i=0
    if adicionar[0] == 'encerrar':
        cdprodutos.sort()
        for c in cdprodutos:
            print(f'{cdprodutos[i]}',end=' ')
            i+=1
        break


