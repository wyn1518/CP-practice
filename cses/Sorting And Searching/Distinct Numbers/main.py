
import sys
import math
from itertools import permutations
# my_str = sys.stdin.readline()
# sys.stdout.write(str(my_str) + "\n")
input = sys.stdin.readline
print = sys.stdout.write

MOD = 1000000007

# approaches: set | sort and count

l = int(input())
n = sorted(list(map(int,input().split())))

ans = 1

for i in range(1,l):
    if n[i-1] != n[i]:
        ans+=1

print(str(ans))



            

    