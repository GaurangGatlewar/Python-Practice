# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        levels = []
        q1 = [root]
        q2 = []
        temp = 0
        while (len(q1)>0):
            node = q1.pop(0)
            temp += node.val
            if node.left: q2.append(node.left)
            if node.right: q2.append(node.right)
            if len(q1)==0:
                levels.append(temp)
                temp = 0
                q1,q2 = q2,q1
        maxSum = levels[0]
        maxLevel = 0
        for i in range(1,len(levels)):
            if levels[i]>maxSum:
                maxSum = levels[i]
                maxLevel = i
        return maxLevel+1