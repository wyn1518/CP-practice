
import sys


t = int(input())
while t > 0:
    n, c, d = map(int, input().split())
    a = map(int,input().split())
    a_sorted = sorted(a)
    a_sorted = [0] + a_sorted
    n = len(a_sorted)
    ans = min(n*c,d*(a_sorted[-1] - (n)))
    dups = 0
    missing = 0
    for i in range(-1,-n,-1):    
        # f = a_sorted[i]
        # s = a_sorted[i-1]
        print(i)
    t-=1
