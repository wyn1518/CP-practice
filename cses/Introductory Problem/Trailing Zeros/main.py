
import sys
import math
# my_str = sys.stdin.readline()
# sys.stdout.write(str(my_str) + "\n")
input = sys.stdin.readline
print = sys.stdout.write

MOD = 1000000007

n = int(input())
ans = 0
f = 5
while n / f > 0:
    ans += int(n / f) 
    f *= 5

print(str(ans))