# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class LowestCommonAncestor:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root == p) or (root == q):
            return root
        
        root.val = self.helper(root, p, q)
        
        while root:
            if (root.left) and (root.left.val[1] == 2):
                root = root.left
            elif (root.right) and (root.right.val[1] == 2):
                root = root.right
            else:
                break
        root.val = root.val[0]
        return root
        
    def helper(self, root, p, q):
        if not root:
            return [0, 0]
        
        answer = 0
        if root.left:
            root.left.val = [root.left.val, self.helper(root.left, p, q)[1]]
            answer += root.left.val[1]
        if root.right:
            root.right.val = [root.right.val, self.helper(root.right, p, q)[1]]
            answer += root.right.val[1]
        
        return [root.val, (answer + (root == p) + (root == q))]