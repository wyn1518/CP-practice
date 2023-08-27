
import sys
import math
import bisect
from itertools import permutations
# my_str = sys.stdin.readline()
# sys.stdout.write(str(my_str) + "\n")
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

    # def search(self,word):
    #     node = self.root
    #     for char in word:
    #         if char not in node.character:
    #             return False
    #         node = node.character[char]

    #     return node.end
    
    # def pref(self,word):
    #     node = self.root
    #     for char in word:
    #         if char not in node.character:
    #             return False
    #         node = node.character[char]

    #     return True

test = Trie()
test.insert('hello')
test.insert('hell')
