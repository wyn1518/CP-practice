
import sys
# my_str = sys.stdin.readline()
# sys.stdout.write(str(my_str) + "\n")
input = sys.stdin.readline
print = sys.stdout.write

MOD = 1000000007
n = int(input())
ans = 1

for i in range(n):
    ans *= 2
    ans %= MOD

print(str(ans))
    