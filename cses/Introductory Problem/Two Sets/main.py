
import sys
# my_str = sys.stdin.readline()
# sys.stdout.write(str(my_str) + "\n")
input = sys.stdin.readline
print = sys.stdout.write

# 0 0 = 0
# 1 1 = 0
# 2 2 = 6
# 3 3 = 6 * 4

n = int(input())
total = int(((n+1)*n)/2)

# print(str(total))
# 1 2 3 4 5 6 7 
# 1 2 5 6
# 3 4 7

# 1 2 3 4 5 6 7 8
# 1 4 5 8

if total % 2 == 1:
    print('NO')
else:
    print('YES\n')
    l1 = []
    l2 = []
    if n % 2 == 0:
        for i in range(1,n + 1,4):
            l1.append(i)
            if i + 3 <= n:
                l1.append(i+3)

        
        for i in range(2,n + 1,4):
            l2.append(i)
            if i + 1 <= n:
                l2.append(i+1)
        

    else:
        for i in range(1,n + 1,4):
            l1.append(i)
            if i + 1 <= n:
                l1.append(i+1)
        
        for i in range(3,n + 1,4):
            l2.append(i)
            if i + 1 <= n:
                l2.append(i+1)

    print(str(len(l1)) + '\n')
    for el in l1:
        print(str(el) + ' ')
    print('\n')
    print(str(len(l2)) + '\n')
    for el in l2:
        print(str(el) + ' ')

