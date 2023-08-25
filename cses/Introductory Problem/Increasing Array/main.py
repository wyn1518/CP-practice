
import sys
# my_str = sys.stdin.readline()
# sys.stdout.write(str(my_str) + "\n")
input = sys.stdin.readline
print = sys.stdout.write

l = int(input())
n = list(map(int,input().split()))

ans = 0;
for i in range(1,l):
    if n[i-1] > n[i]:
        temp = n[i-1] - n[i]
        ans += temp
        n[i] += temp;

print(str(ans))