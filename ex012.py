inicio = int(input())
fim = int(input())
counter = 0
if inicio < 2:
    inicio = 2
for i in range(inicio, fim + 1):
    for x in range(2, i):
        if i % x == 0:
            break
    else:
        counter += 1
        print(f"{i}")
print(f"primos: {counter}")
        
