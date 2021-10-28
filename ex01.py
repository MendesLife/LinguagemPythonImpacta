desctfixo = 0.1
descvaria = 0.01
valor = float(input())
qtde = int(input())
valorcompra = qtde*valor
desctotal = desctfixo+(descvaria*qtde)
valordesconto = valorcompra-(valorcompra*desctotal)
print(f'{valorcompra:.2f}')
print(f'{valordesconto:.2f}')