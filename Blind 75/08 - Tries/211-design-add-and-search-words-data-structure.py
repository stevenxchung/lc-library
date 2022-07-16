'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the test class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
'''
from time import time


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def dfs_helper(self, word: str, position: int, root: TrieNode):
        node = root
        for i in range(position, len(word)):
            c = word[i]
            if c == '.':
                for child in node.children.values():
                    if self.dfs_helper(word, i + 1, child):
                        # Found word
                        return True
                    return False
            else:
                if c not in node.children:
                    return False
                node = node.children[c]

        return node.is_end

    def search(self, word: str) -> bool:
        res = self.dfs_helper(word, 0, self.root)
        print(res)
        return res


if __name__ == '__main__':
    test = WordDictionary()
    sol_start = time()
    test.addWord("bad")
    test.addWord("dad")
    test.addWord("mad")
    test.search("pad")  # return False
    test.search("bad")  # return True
    test.search(".ad")  # return True
    test.search("b..")  # return True
    print(f'Runtime for our solution: {time() - sol_start}')
