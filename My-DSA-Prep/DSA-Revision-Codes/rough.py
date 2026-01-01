'''
author : Rudrasena Reddy
date : 07.12.2025

purpose : Just to practice rough work.
'''

# Rough code here

a = '1100001001000010000001'
maxi = 0
cur = 0

for i in a:
    if i =='0':
        cur += 1
    else:
        cur = 0
    maxi = max(maxi,cur)
print(maxi)
