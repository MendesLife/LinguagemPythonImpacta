lista_tempos=[]
while True:
    tempo=int(input())
    if tempo > 0:
        lista_tempos.append(tempo)
    if tempo < 0:
        break
media = sum(lista_tempos)/len(lista_tempos)
print(f'MEDIA: {media:.2f}')
for c in lista_tempos:
    if c < media:
        print(c)
        