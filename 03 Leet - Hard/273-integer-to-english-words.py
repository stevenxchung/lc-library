'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.
'''


class Solution:
    def __init__(self):
        # Starts from zero, create arrays for each category
        self.underTwenty = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                            'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

        self.tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty',
                     'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

        self.thousandPlus = ['', 'Thousand', 'Million', 'Billion']

    def numberToWords(self, num):
        if num == 0:
            return 'Zero'

        words = ''
        # Since the upper limit of num breaks down after dividing by 1000 four times we use len(self.thousandPlus)
        for i in range(len(self.thousandPlus)):
            if num % 1000 != 0:
                #  Insert remainder into helper
                words = self.helper(num % 1000) + \
                    self.thousandPlus[i] + ' ' + words
            print(num)
            # Must use // to get integer value
            num //= 1000
        return words.strip()

    # Recursively breaks down number into categories
    def helper(self, num):
        if num == 0:
            return ''
        elif num < 20:
            return self.underTwenty[num] + ' '
        elif num < 100:
            return self.tens[num // 10] + ' ' + self.helper(num % 10)
        else:
            return self.underTwenty[num // 100] + ' Hundred ' + self.helper(num % 100)


sol = Solution()
# Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven
print(sol.numberToWords(2147483647))
# print(sol.numberToWords(123))
