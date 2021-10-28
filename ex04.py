n = int(input())
if n>=2:
    if n%2 == 0:
        print(f'{n-1} {n+2}')
    else:
        print(f'{n-2} {n+1}')