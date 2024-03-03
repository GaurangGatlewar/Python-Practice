# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class RightSideView:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        view = []
        q1 = [root]
        q2 = []
        temp = []
        while (len(q1)>0):
            node = q1.pop(0)
            temp.append(node.val)
            if node.left: q2.append(node.left)
            if node.right: q2.append(node.right)
            if len(q1) == 0:
                view.append(temp)
                temp = []
                q1,q2 = q2,q1
        return ([x[-1] for x in view])