#https://leetcode.com/problems/group-anagrams/

#Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
#Output:
#[
#  ["ate","eat","tea"],
#  ["nat","tan"],
#  ["bat"]
#]

class Solution:

    def buildKey(self, word):
        orig_key = [0] * (ord('z') - ord('a') + 1)

        for c in word:
            idx = ord(c) - ord('a')
            orig_key[idx] += 1

        return str(orig_key)

    def groupAnagrams(self, strs):
        result_dict = {}

        for s in strs:
            str_key = self.buildKey(s)
            if str_key not in result_dict.keys():
                result_dict[str_key] = []

            result_dict[str_key].append(s)

        return result_dict.values()


sln = Solution()

print(sln.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
