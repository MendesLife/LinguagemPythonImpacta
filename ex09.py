c=0
while True:
    vcoin = float(input())
    if vcoin == -1:
        break
    c=c+vcoin
print(f'VC$ {c:.2f}')
print(f'R$ {c*2.50:.2f}')