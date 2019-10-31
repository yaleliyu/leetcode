class Solution:
    def numDecodings(self, s: str) -> int:
        int_s = [int(c) for c in s]

        ways_cnt = [-1] * (len(int_s)+1)
        ways_cnt[-1] = 1
        ways_cnt[-2] = 1 if int_s[-1] > 0 else 0
        for idx in range(len(int_s)-2, -1, -1):
            if int_s[idx] > 2:
                ways_cnt[idx] = ways_cnt[idx+1]
            elif int_s[idx] == 2:
                if int_s[idx+1] <= 6:
                    ways_cnt[idx] = ways_cnt[idx+1] + ways_cnt[idx+2]
                else:
                    ways_cnt[idx] = ways_cnt[idx+1]
            elif int_s[idx] == 1:
                ways_cnt[idx] = ways_cnt[idx+1] + ways_cnt[idx+2]
            elif int_s[idx] == 0:
                ways_cnt[idx] = 0

        return ways_cnt[0]

sln = Solution()
print(sln.numDecodings('99'))

print(sln.numDecodings('27'))
print(sln.numDecodings('06'))
print(sln.numDecodings('0'))
print(sln.numDecodings('226'))
print(sln.numDecodings('1226'))
