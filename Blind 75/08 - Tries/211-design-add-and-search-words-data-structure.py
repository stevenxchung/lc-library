'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the test class:

- WordDictionary() Initializes the object.
- void addWord(word) Adds word to the data structure, it can be matched later.
- bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
'''

from time import time


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self, debug=False):
        self.debug = debug
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                # End of the word
                return node.is_end
            elif word[i] == '.':
                for child in node.children.values():
                    # Search all child nodes
                    if dfs(i + 1, child):
                        return True
                return False

            if word[i] not in node.children:
                return False
            node = node.children[word[i]]

            return dfs(i + 1, node)

        res = dfs(0, self.root)
        if self.debug:
            return print(f'search({word}): {res}')
        return res


if __name__ == '__main__':
    test = WordDictionary(debug=True)
    sol_start = time()
    test.addWord('bad')
    test.addWord('dad')
    test.addWord('mad')
    test.search('pad')  # Return False
    test.search('bad')  # Return True
    test.search('.ad')  # Return True
    test.search('b..')  # Return True
    print(f'Runtime for our solution: {time() - sol_start}\n')

    # Additional
    print('\nAdditional testing...')
    test = WordDictionary(debug=True)
    test.addWord('a')
    test.addWord('a')
    # true, true, false, true, false, false
    test.search('.')
    test.search('a')
    test.search('aa')
    test.search('a')
    test.search('.a')
    test.search('a.')

    test.addWord('at')
    test.addWord('and')
    test.addWord('an')
    test.addWord('add')
    # true, false
    test.search('a')
    test.search('.at')

    test.addWord('bat')
    # true, true, false, false, true, true
    test.search('.at')
    test.search('an.')
    test.search('a.d.')
    test.search('b.')
    test.search('a.d')
    test.search('.')
    print(f'Runtime for our solution: {time() - sol_start}')
