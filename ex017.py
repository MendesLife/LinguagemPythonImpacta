notas_originais=[]
notas_alteradas=[]
contador=000
qtde_alterada = 0
N=int(input())
if (1 <= N <= 999):
    for c in range(0,N):
        nota=float(input())
        notas_originais.append(nota)
    for c in range(0,N):
        segunda_chance=float(input())
        notas_alteradas.append(segunda_chance)
        if segunda_chance == 10.00 and notas_originais[c] < 10.00:
            qtde_alterada+=1
    print(f'NOTAS ALTERADAS: {qtde_alterada}')
    for c in range(0,N):
        if notas_alteradas[c] == 10.00 and notas_originais[c] < 10.00:
            indicador = '*'
            soma = notas_originais[c] + 2
            if soma > 10:
                soma = 10.00
        else:
            indicador='-'
            soma = notas_originais[c]
        print(f'{indicador}({contador+1:0>3}) original: {notas_originais[c]:0^5} | final: {soma:0^5}')
        contador+=1