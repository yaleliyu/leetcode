# https://leetcode.com/problems/maximum-width-ramp/

class Solution:
    #def maxWidthRampImpl(self, A, start, end):

    def __init__(self):
        self.buf = []

    def maxWidthRamp(self, A) -> int:

        result = 0

        for idx in range(1, len(A)):
            if A[idx] > A[idx-1]:
                result += 1
            else:
                right_result = self.maxWidthRamp(A[idx:])
                result = max(result, right_result)

        return result

sln = Solution()
print(sln.maxWidthRamp([6,0,8,2,1,5]))
