n1= float(input()) 
n2= float(input())
if n1 >=0 and n1 <=10 and n2 >=0 and n2 <=10:
    media = (n1+n2)/2
    if media >= 6:
        print('aprovado')
    elif n1>=2 and media<6:
        print('talvez com a sub')
    else:
        print('reprovado')