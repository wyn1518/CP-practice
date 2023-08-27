
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
    class Node:
        def __init__(self):
            self.character = {}
            self.end = False


    class Trie:
        def __init__(self):
            self.root = Node()

        def insert(self,word):
            node = self.root
            for char in word:
                if char not in node.character:
                    node.character[char] = Node()
                node = node.character[char]
            node.end = True

        def search(self,word):
            l = len(word)
            ans = [0]* (l + 1) 
            ans[l] = 1
            for i in range(l-1,-1,-1):
                node = self.root
                for j in range(i,l):
                    if word[j] not in node.character:
                        break
                    node = node.character[word[j]]
                    if node.end:
                        ans[i] = (ans[i]%MOD + ans[j + 1]%MOD)%MOD
            print(str(ans[0]))
        

    word = str(input())[:-1]
    n = int(input())
    trie = Trie()

    for _ in range(n):
        temp = str(input())[:-1]
        trie.insert(temp)

    trie.search(word)
main()