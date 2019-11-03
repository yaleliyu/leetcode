class Solution:

    def calculateIndent(self, numerator: int, denominator: int):
        cnt = 0
        while pow(10, cnt+1) * numerator < denominator:
            cnt += 1

        return cnt

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        int_p = int(numerator/denominator)
        mod_p = abs(numerator) % abs(denominator)

        if mod_p == 0:
            return str(int_p)

        result = str(int_p) + '.'
        mod_p_list = [mod_p]
        while True:
            indent = self.calculateIndent(mod_p, denominator)
            result += '0'*indent
            result += str(int((mod_p * pow(10, indent+1)) / denominator))
            new_mod_p = (mod_p * pow(10, indent+1)) % denominator

            if new_mod_p == 0:
                break

            if new_mod_p in mod_p_list:
                idx = mod_p_list.index(new_mod_p)
                pnt_idx = result.index('.')
                left_brackt_pos = pnt_idx + idx + 1
                result = result[:left_brackt_pos] + '(' + result[left_brackt_pos:]

                result = result + ')'
                break

            mod_p_list.append(new_mod_p)
            mod_p = new_mod_p


        return result

sln = Solution()
print(sln.fractionToDecimal(-50, 8))
print(sln.fractionToDecimal(1, 23))
print(sln.fractionToDecimal(1, 2))
print(sln.fractionToDecimal(2, 1))
print(sln.fractionToDecimal(2, 3))
print(sln.fractionToDecimal(1, 23))
