# https://leetcode.com/problems/kth-ancestor-of-a-tree-node/

class TreeAncestor:
    class TreeNode:
        def __init__(self, val: int, subNodes):
            self.val = val
            self.subNodes = subNodes

    def __init__(self, n: int, parent):
        self.parentDict = {'0':[0]}
        self.buildTree(n, parent)

    def buildTree(self, n: int, parent):
        for val, p in enumerate(parent[1:]):
            parentNodes = self.parentDict[str(p)]
            self.parentDict[str(val+1)] = [val+1] + parentNodes


    def getKthAncestor(self, node: int, k: int) -> int:
        if str(node) not in self.parentDict.keys():
            return -1

        result = -1
        parentsNode = self.parentDict[str(node)]
        if len(parentsNode) > k:
            result = parentsNode[k]

        return result



# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
obj = TreeAncestor(7,[-1,0,0,1,1,2,2])
print(obj.getKthAncestor(3, 1))
print(obj.getKthAncestor(5, 2))
print(obj.getKthAncestor(6, 3))

obj = TreeAncestor(5,[-1,0,0,0,3])
print(obj.getKthAncestor(1, 5))
print(obj.getKthAncestor(3, 2))
print(obj.getKthAncestor(0, 1))
print(obj.getKthAncestor(3, 1))
print(obj.getKthAncestor(3, 5))