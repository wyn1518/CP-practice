
import sys
# import math
# import bisect
# from itertools import permutations
# my_str = sys.stdin.readline()
# sys.stdout.write(str(my_str) + "\n")

# TLE
def main():

    input = sys.stdin.readline
    print = sys.stdout.write
    MOD = 1000000007

    n, x = list(map(int,input().split()))
    c = list(map(int,input().split()))
    rec =  [100000000] * (x+1)
    rec[0] = 0
    for i in range(0,x+1):
        for el in c:
            if i + el <= x:
                rec[i+el] = min(rec[i]+1,rec[i+el])
    print(str(-1 if rec[x] == 100000000 else rec[x]))
main()