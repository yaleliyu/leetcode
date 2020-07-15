# https://leetcode.com/problems/longest-duplicate-substring/

class Solution:
    class TreeNode:
        def __init__(self):
            self.data = [None] * 26

    def __init__(self):
        self.headNode = self.TreeNode()
        self.dupString = ''

    def getIndex(self, ch:str):
        return ord(ch) - ord('a')

    def addNewString(self, s:str):
        if len(s) <= len(self.dupString):
            return

        isMatch = False
        currentDup = ''
        nodeData = self.headNode.data
        for i, ch in enumerate(s):
            index = self.getIndex(ch)
            if nodeData[index] is None:
                nodeData[index] = self.TreeNode()
                isMatch = False
                nodeData = nodeData[index].data
            else:
                nodeData = nodeData[index].data
                if i == 0:
                    isMatch = True
                if isMatch:
                    currentDup += ch
        self.dupString = self.dupString if len(self.dupString) > len(currentDup) else currentDup

    def longestDupSubstring(self, S: str) -> str:
        for index, c in enumerate(S):
            self.addNewString(S[index:])

        return self.dupString



sln = Solution()
print(sln.longestDupSubstring('abracadabrac'))
