'''
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
'''
from time import time


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        return ''.join([f'{len(s)}#{s}' for s in strs])

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        output = []
        length = 0
        i1, i2 = 0, 0
        while i1 < len(str):
            prefix = ''
            while str[i2] != '#':
                prefix += str[i2]
                i2 += 1

            i1 = i2 + 1
            length = int(prefix)
            output.append(str[i1:i1 + length])

            i1 += length
            i2 = i1

        return output

    def encode_reference(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode_reference(self, str):
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1: j + 1 + length])
            i = j + 1 + length
        return res

    def quantify(self, test_cases, runs=100000):
        sol_start = time()
        for i in range(runs):
            for case in test_cases:
                if i == 0:
                    encoded = self.encode(case)
                    decoded = self.decode(encoded)
                    print(encoded, decoded)
                else:
                    self.encode(case)
                    self.decode(encoded)
        print(f'Runtime for our solution: {time() - sol_start}\n')

        ref_start = time()
        for i in range(0, runs):
            for case in test_cases:
                if i == 0:
                    encoded = self.encode_reference(case)
                    decoded = self.decode_reference(encoded)
                    print(encoded, decoded)
                else:
                    self.encode_reference(case)
                    self.decode_reference(encoded)
        print(f'Runtime for reference: {time() - ref_start}\n')


if __name__ == '__main__':
    test = Solution()
    test_cases = [
        ["lint", "code", "love", "you"],
        ["we", "say", ":", "yes"]
    ]
    test.quantify(test_cases)
