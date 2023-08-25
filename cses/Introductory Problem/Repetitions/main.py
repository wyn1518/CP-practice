
import sys
# my_str = sys.stdin.readline()
# sys.stdout.write(str(my_str) + "\n")
input = sys.stdin.readline
print = sys.stdout.write

s = input()
ans = 1
temp = 1
# Every exsiting character in a string have a minimum count of 1
for i in range(1,len(s)-1):
    if s[i-1] == s[i]:
        temp += 1
    elif s[i-1] != s[i]:
        temp = 1
        
    ans = max(temp,ans)

print(str(ans))