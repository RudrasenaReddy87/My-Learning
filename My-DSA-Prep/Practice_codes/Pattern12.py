n = int(input())
for i in range(1,n+1):
    s = 0
    x = 0
    space = n*2 
    for j in range(1,i+1):
        s =j + s * 10
        space-=1
    for k in range(i,0,-1):
        x = x*10 + k
        space-=1
    print(s," "*space,x,sep='')

