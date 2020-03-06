# https://leetcode.com/problems/valid-number/

class Solution:
    def __init__(self):
        self.numbers = set([str(i) for i in range(0, 10)])
        self.signs = ['-', '+']

    def isInteger(self, s:str) -> bool:
        s = s.strip()
        if len(s) == 0:
            return False

        number_found = False
        is_int = True

        for idx, c in enumerate(s):
            if c in self.numbers:
                number_found = True

            if idx == 0:
                if c not in self.signs and c not in self.numbers:
                    is_int = False
                    break
            else:
                if c not in self.numbers:
                    is_int = False
                    break

        return is_int and number_found

    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if len(s) == 0:
            return False

        is_number = True
        point_found = False
        number_found = False
        for idx, c in enumerate(s):
            if c in self.numbers:
                number_found = True

            if idx == 0:
                if c not in self.signs and c not in self.numbers and c!='.':
                    is_number = False
                    break

                if c == '.':
                    point_found = True

                    if len(s) == 1 or (len(s)>1 and s[1] not in self.numbers):
                        is_number = False
                        break

                if c in self.signs:
                    if len(s) == 1:
                        is_number = False
                        break
            else:
                if c == 'e':
                    is_number = self.isInteger(s[idx+1:])
                    break
                elif c == '.':
                    if point_found:
                        is_number = False
                        break
                    point_found = True
                elif c not in self.numbers:
                    is_number = False
                    break

        return is_number and number_found


sln = Solution()
# "0" => true
print(sln.isNumber('0'))
# " 0.1 " => true
print(sln.isNumber('0.1'))
# "abc" => false
print(sln.isNumber('abc'))
# "1 a" => false
print(sln.isNumber('1 a'))
# "2e10" => true
print(sln.isNumber('2e10'))
# " -90e3   " => true
print(sln.isNumber(' -90e3   '))
# " 1e" => false
print(sln.isNumber(' 1e'))
# "e3" => false
print(sln.isNumber('e3'))
# " 6e-1" => true
print(sln.isNumber(' 6e-1'))
# " 99e2.5 " => false
print(sln.isNumber(' 99e2.5 '))
# "53.5e93" => true
print(sln.isNumber('53.5e93'))
# " --6 " => false
print(sln.isNumber(' --6 '))
# "-+3" => false
print(sln.isNumber('-+3'))
# "95a54e53" => false
print(sln.isNumber('95a54e53'))
# "0.." => false
print(sln.isNumber('0..'))
