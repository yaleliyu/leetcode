# https://leetcode.com/problems/longest-valid-parentheses/

# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left_stack = []
        result = []

        for idx, c in enumerate(s):
            if c == '(':
                left_stack.append([idx, c])

            if c == ')':
                if len(left_stack) > 0:
                    v = left_stack.pop()
                    result.append([v[0], idx])

        if len(result) == 0:
            return 0

        result.sort(key=lambda pair : pair[0])

        current_left = result[0][0]
        current_right = result[0][1]

        max = 0
        acc = current_right - current_left + 1
        for pair in result[1:]:
            if pair[0] > current_right:
                if pair[0] == current_right+1:
                    acc += pair[1] - pair[0] + 1
                else:
                    max = acc if max < acc else max
                    acc = pair[1] - pair[0] + 1

                current_left = pair[0]
                current_right = pair[1]

        max = acc if max < acc else max

        return max

sln = Solution()
print(sln.longestValidParentheses("()((())()"))
print(sln.longestValidParentheses('(()'))
