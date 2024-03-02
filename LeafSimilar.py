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
        leafSequence = []
        if root: 
            q = [root]
            while len(q)>0:
                currentNode = q.pop()
                if not currentNode.left and not currentNode.right:
                    leafSequence.append(currentNode.val)
                if currentNode.right:
                    q.append(currentNode.right)
                if currentNode.left:
                    q.append(currentNode.left)
        return leafSequence