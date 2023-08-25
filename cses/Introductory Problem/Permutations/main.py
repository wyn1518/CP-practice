
import sys
# my_str = sys.stdin.readline()
# sys.stdout.write(str(my_str) + "\n")
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
if n == 3 or n == 2:
    print('NO SOLUTION')
else:
    
    for i in range(2,n + 1,2):
        print(str(i) + ' ')
    for i in range(1,n + 1,2):
        print(str(i) + ' ')
