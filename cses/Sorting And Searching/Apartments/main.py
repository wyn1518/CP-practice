
import sys
import math
from itertools import permutations
# my_str = sys.stdin.readline()
# sys.stdout.write(str(my_str) + "\n")
input = sys.stdin.readline
print = sys.stdout.write

MOD = 1000000007

# 4 3 5
# 60 45 80 60
# 30 60 75

# 45 60 60 80
# 30 60 75
#   

n,m,k = list(map(int,input().split()))
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())))
# print(str(a) + '\n')
# print(str(b) + '\n')
ans = 0
i = 0
j = 0
while j < n and i < m:
    
    # print(str(a[j]) + ' ' + str(b[i]) + '\n')
    if a[j] >= b[i] - k:
        
        if a[j] <= b[i] + k:
            ans+= 1
            j+=1
            i+= 1
        else:
            i+=1

    else:
        j+=1



print(str(ans))

            

    