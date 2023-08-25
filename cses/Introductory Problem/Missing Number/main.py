
import sys
# my_str = sys.stdin.readline()
# sys.stdout.write(str(my_str) + "\n")
input = sys.stdin.readline
print = sys.stdout.write

l = int(input())
n = list(map(int,input().split(' ')))
s = 0
for i in n:
    s += i

print(str(int(((l+1)*l)/2 - s)))