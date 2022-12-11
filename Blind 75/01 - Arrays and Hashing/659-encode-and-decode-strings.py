'''
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
'''
from time import time


class Solution:
    def encode(self, strs):
        '''
        @param: strs: a list of strings
        @return: encodes a list of strings to a single string.
        '''
        return ''.join([f'{len(s)}#{s}' for s in strs])

    def decode(self, str):
        '''
        @param: str: A string
        @return: decodes a single string to a list of strings
        '''
        res = []
        length = 0
        i1, i2 = 0, 0
        while i1 < len(str):
            prefix = ''
            while str[i2] != '#':
                prefix += str[i2]
                i2 += 1

            i1 = i2 + 1
            length = int(prefix)
            res.append(str[i1 : i1 + length])

            i1 += length
            i2 = i1

        return res

    def encode_reference(self, strs):
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode_reference(self, str):
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != '#':
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res

    def quantify(self, test_cases, runs=50000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                encoded = self.encode(case)
                decoded = self.decode(encoded)
                if i == 0:
                    print(encoded, decoded)
        print(f'Runtime for our solution: {time() - sol_start}\n')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                encoded = self.encode_reference(case)
                decoded = self.decode_reference(encoded)
                if i == 0:
                    print(encoded, decoded)
        print(f'Runtime for reference: {time() - ref_start}')


if __name__ == '__main__':
    test = Solution()
    test_cases = [['lint', 'code', 'love', 'you'], ['we', 'say', ':', 'yes']]
    test.quantify(test_cases)
