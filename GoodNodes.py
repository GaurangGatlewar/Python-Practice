# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class GoodNodes:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesHelper(root, float(-inf))

    def goodNodesHelper(self, root: TreeNode, limit: int) -> int:
        if not root: return 0
        count = 0
        count += (root.val>=limit)
        count += self.goodNodesHelper(root.left,max(root.val,limit))
        count += self.goodNodesHelper(root.right,max(root.val,limit))
        return count