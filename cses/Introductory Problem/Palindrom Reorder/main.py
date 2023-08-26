
import sys
import math
# my_str = sys.stdin.readline()
# sys.stdout.write(str(my_str) + "\n")
input = sys.stdin.readline
print = sys.stdout.write

MOD = 1000000007


s = str(input())
m = {}
for l in s:
    if l == '\n':
        continue
    if l not in m:
        m[l] = 1
    else:
        m[l]+=1

odd = 0
oneOddLetter = ''
oneOddLetterValue = 0
for k,v in m.items():
    if v % 2 == 1:
        odd+=1
        oneOddLetter = k
        oneOddLetterValue = v

if odd > 1:
    print("NO SOLUTION")
else:
    ans = ''
    for k,v in m.items():
        if k == oneOddLetter:
            continue
        ans += ''.ljust(int(v/2),k)
        
    if oneOddLetter != '':
        print(ans + ''.ljust(oneOddLetterValue,oneOddLetter) + ans[::-1])
    else:
        print(ans + ans[::-1])
