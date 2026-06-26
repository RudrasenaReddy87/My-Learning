n = int(input())
for i in range(1,n+1):
    s = ''
    for j in range(1,i+1):
        print("*",s)
        if s=='':
            s='1'
        elif s[0]=='1':
            s = '0'+s
        else:
            s = '1'+s
    print(s)

# if starting 0 then add 1 at front
# if starting 1 then add 0 at front
