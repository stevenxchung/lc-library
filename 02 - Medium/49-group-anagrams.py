'''
Given an array of strings, group anagrams together.
'''


class Solution:
    def groupAnagrams(self, strs):
        kVStore = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key not in kVStore:
                kVStore[key] = [str]
            else:
                kVStore[key] += [str]

        return kVStore.values()


input = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
sol = Solution()
print(sol.groupAnagrams(input))
