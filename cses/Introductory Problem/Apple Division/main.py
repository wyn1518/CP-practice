
import sys
import math
from itertools import permutations
# my_str = sys.stdin.readline()
# sys.stdout.write(str(my_str) + "\n")
input = sys.stdin.readline
print = sys.stdout.write

MOD = 1000000007

# 3 2 7 4 1
# l l l l l l

n = int(input())
l = list(map(int,input().split()))

def solve(i,s1,s2):
    if(i == n):
        return abs(s1-s2)
    else:
        return min(solve(i+1,s1 + l[i],s2),solve(i+1,s1,s2 + l[i]))

print(str(solve(0,0,0)))



            

    