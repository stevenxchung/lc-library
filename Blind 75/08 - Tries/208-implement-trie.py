'''
A trie (pronounced as 'try') or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
'''

from time import time


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self, debug=False):
        self.debug = debug
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root

        for c in word:
            if c not in node.children:
                if self.debug:
                    return print(f'search({word}): {False}')
                return False
            node = node.children[c]

        res = node.is_end
        if self.debug:
            return print(f'search({word}): {res}')
        return res

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for c in prefix:
            if c not in node.children:
                if self.debug:
                    return print(f'startsWith({prefix}): {False}')
                return False
            node = node.children[c]

        if self.debug:
            return print(f'startsWith({prefix}): {True}')
        return True


if __name__ == '__main__':
    test = Trie(debug=True)
    sol_start = time()
    test.insert('apple')
    test.search('apple')  # Return True
    test.search('app')  # Return False
    test.startsWith('app')  # Return True
    test.insert('app')
    test.search('app')  # Return True
    print(f'Runtime for our solution: {time() - sol_start}\n')
