total = int(input())
mensal = int(input())
for i in range(0,total,mensal):
    if i == 0:
        c=0
    c+=1
    print(f'pagamento: {c}')
    print(f'antes = {total-i}')
    if total-(mensal*c) < 0:
        print('depois = 0')
    else:
        print(f'depois = {total-(mensal*c)}')
    print('-----')