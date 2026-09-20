# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def dfs(curr):
            if curr is None : return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            if left == float('-inf') or right== float('-inf') or abs(left - right) > 1 : return float('-inf')
            return 1 + max(left , right)
            
        return dfs(root)!=float('-inf')