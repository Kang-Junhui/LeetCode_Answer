# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            self.res += root.val
            root.val = self.res
            self.bstToGst(root.left)
            
        return root
