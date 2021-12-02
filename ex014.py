A = int(input())
B = int(input())
if A > B:
    print("Nenhuma tabuada no intervalo!")
else:
    while A <= B:
        for c in range(1,11):
            print(f"{A} x {c} = {A*c}")
        print("-"*10)
        A+=1