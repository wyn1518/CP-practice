
import sys
# my_str = sys.stdin.readline()
# sys.stdout.write(str(my_str) + "\n")
input = sys.stdin.readline
print = sys.stdout.write


n = int(input())
print(str(n))
print(' ')
while n > 1:
    n = n*3+1 if n%2==1 else int(n/2)
    print(str(n))
    print(' ')