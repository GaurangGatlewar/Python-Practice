# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class LeafSimilar:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = self.findLeafSequence(root1)
        leaves2 = self.findLeafSequence(root2)
        return leaves1==leaves2

    def findLeafSequence(self, root: Optional[TreeNode]) -> List:
        if not root:
            return ([])

        if not root.left and not root.right:
            return ([root.val])

        if not root.left:
            return self.findLeafSequence(root.right)

        if not root.right:
            return self.findLeafSequence(root.left)

        sequence1 = self.findLeafSequence(root.left)
        sequence2 = self.findLeafSequence(root.right)
        sequence1.extend(sequence2)
        return (sequence1)