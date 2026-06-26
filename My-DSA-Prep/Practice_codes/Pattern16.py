n = int(input())
for i in range(1,n+1):
    front = ''
    last = ''
    c = 0
    space = n-i
    for j in range((i*2)//2):
        front+=chr(65+j)
        if j>=1:
            last = front[c] + last
            c += 1
    print(" "*space,front,last,sep='')
    
