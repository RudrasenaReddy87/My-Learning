n = int(input())
temp = n
act = n * 2 - 1
ans = ''
# ee roju nee pani avvala repu kachithanga solve chestha pa
# today : 4 june 2026
for i in range(act):
    ass=ans
    for j in range(i,act - i):
        if i==0 or i==(act-1):
            ass+=str(n)
        elif i>(act//2):
            ass+=str(i-n)
        else:
            ass+=str(n-i)
    ans+=str(n-i)
    print(ass+ans[:i][::-1])
