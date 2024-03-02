# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        count = 0
        q = [root]
        while (len(q)>0):
            currentNode = q.pop()
            count += self.continousPathSum(currentNode,targetSum)
            if currentNode.left: q.append(currentNode.left)
            if currentNode.right: q.append(currentNode.right)
        return count

    def continousPathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        count = 0
        count += (root.val == targetSum)
        if root.left:
            count += self.continousPathSum(root.left,targetSum-root.val)
        if root.right:
            count += self.continousPathSum(root.right,targetSum-root.val)
        return count