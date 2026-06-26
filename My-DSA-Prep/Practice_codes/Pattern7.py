n = int(input())
'''
for i in range(1,n+1):
    print(" "*(n-i),"*"*(i+(i-1)))
'''
for i in range(1,n+1):
    for j in range(n-i,0,-1):
        print(" ",end='')
    for k in range(i+(i-1)):
        print("*",end='')
    print()
# for star i observe first star + to next star
# we can think like this also 2nd star - to 1st star
# space i take n-1