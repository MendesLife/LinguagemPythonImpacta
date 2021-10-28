c=0
INÍCIO = int(input())
FIM = int(input())
if(0 <= INÍCIO <= FIM <= 9999):
    for i in range(INÍCIO,FIM+1):
        if i%4==0 and i%100!=0 or i%400==0:
            c+=1
            print(f'{i}')
    print(f'bissextos: {c}')