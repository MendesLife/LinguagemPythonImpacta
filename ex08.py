letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

N = int(input())
if (1 <= N <= 26): 
    
     for i in range (0,N):
         if i == 0:
             print(f'{letras[0]}')
         else:
            print(f'{(letras[i]*(i+1))}')