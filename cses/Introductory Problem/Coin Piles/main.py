
import sys
import math
# my_str = sys.stdin.readline()
# sys.stdout.write(str(my_str) + "\n")
input = sys.stdin.readline
print = sys.stdout.write

MOD = 1000000007

# 2 1
# 1 2
# 2 1
# 2 1
# NO a*2 < b or b*2 < a or 
# 
t = int(input())
while t > 0:

    a,b = list(map(int,input().split()))
    mx = max(a,b)
    mn = min(a,b)
    if mx > 2*mn or (mx+mn)%3 != 0:
        print('NO')
    else:
        print('YES')
    print('\n')
    t-=1
