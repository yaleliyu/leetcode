
# https://leetcode.com/problems/strong-password-checker/

# It has at least 6 characters and at most 20 characters.
# It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
# It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).


class Solution:
    def __init__(self):
        self.lower_cases = set([c for c in 'abcdefghijklmnopqrstuvwxyz'])
        self.upper_cases = set([c.upper() for c in lower_cases])
        self.digit = set([str(c) for c in range(10)])

    def removeDupOp(self, s:str) -> int:

    def strongPasswordCheckerImpl(self, s:str, pos:int, lower_found:bool, upper_found:bool, digit_found:bool) -> int:
        if len(str) <= 3:
            return 6 - len(str)

        if pos >= 20:
            op = len(s) - 20
            if not lower_found:
                op += 1
            if not upper_found:
                op += 1
            if not digit_found:
                op += 1
            return op



    def contains(self, s:str, char_type:set):
        is_contain = False
        for c in str:
            if c in char_type:
                is_contain = True
                break

        return is_contain

    def strongPasswordChecker(self, s: str) -> int:

        lower_found = self.contains(s, self.lower_cases)
        upper_found = self.contains(s, self.upper_cases)
        digit_found = self.contains(s, self.digit)



