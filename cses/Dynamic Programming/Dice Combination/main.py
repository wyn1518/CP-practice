
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
    n = int(input())
    base = [0] * (n+1)
    base[0] = 1
    for i in range(1,n+1):
        for j in range(1,7):
            if i-j >= 0:
                base[i] += base[i-j]
                base[i]%=MOD

    print(str(base[n]))
main()