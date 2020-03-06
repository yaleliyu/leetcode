# https://leetcode.com/problems/jump-game-ii/

import math
class Solution:
    def __init__(self):
        self.best_sln = []


    def jumpRecursive(self, nums, pos):
        for steps in range(1, nums[pos]+1):
            

    def jump(self, nums) -> int:
        self.best_sln = [math.inf] * len(nums)

        for idx, steps in enumerate(nums):
