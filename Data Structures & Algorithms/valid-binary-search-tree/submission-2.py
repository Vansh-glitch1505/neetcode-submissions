# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def validate(self, root, mx, mn):
        if root == None:
            return True
        if root.val > mx or root.val < mn:
            return False
        
        leftCheck = self.validate(root.left, root.val - 1, mn)
        rightCheck = self.validate(root.right, mx, root.val + 1)

        return leftCheck and rightCheck

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return(self.validate(root, 1000000000, -100000000))
        