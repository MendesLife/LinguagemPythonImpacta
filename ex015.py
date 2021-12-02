N=int(input())
lista_dados=[]
if(1 <= N <= 200):
    for i in range(0,N):
        dados=input().split(';')
        dados[0]=str(dados[0])
        dados[1]=int(dados[1])
        dados[2]=float(dados[2])
        dados[3]=str(dados[3])
        lista_dados.append(dados)
    X=float(input())
    Y=float(input())
    print('-----')
    print('BÔNUS')
    print('-----')
    for a in range(0,N):
        if lista_dados[a][3] == 'sim' and lista_dados[a][1] >= 1000:
            valor= ((((lista_dados[a][1])//1000)*X)+lista_dados[a][2]) 
        if lista_dados[a][3] == 'não' and lista_dados[a][1] >= 1000:
            valor= ((((lista_dados[a][1])//1000)*Y)+lista_dados[a][2])
        if lista_dados[a][1] < 1000 and lista_dados[a][2] == 0.00:
            valor = lista_dados[a][2]
        if lista_dados[a][1] < 1000:
            valor = lista_dados[a][2]
        print(f'{lista_dados[a][0]}: R$ {valor:.2f}')
    