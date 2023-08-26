
import sys
import math
from itertools import permutations
# my_str = sys.stdin.readline()
# sys.stdout.write(str(my_str) + "\n")
input = sys.stdin.readline
print = sys.stdout.write

MOD = 1000000007

n,x = list(map(int,input().split()))
p = sorted(list(map(int,input().split())))

l = 0
r = n - 1
ans = 0
while l <= r:
    if p[l] + p[r] <= x:
        ans+= 1
        l+= 1
        r-= 1
    elif p[r] <= x:
        ans+= 1
        r-= 1
        
print(str(ans))


            

    