
import sys
import math
from itertools import permutations
# my_str = sys.stdin.readline()
# sys.stdout.write(str(my_str) + "\n")
input = sys.stdin.readline
print = sys.stdout.write

MOD = 1000000007

s = str(input())[:-1]
s = ''.join(sorted(s))
p = set(map( lambda x:''.join(x) , list(permutations(s))))
print(str(len(p)) + '\n')
for el in p:
    print(el + '\n')