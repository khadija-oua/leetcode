# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None : return True 
        def dfs(curr1,curr2):
            if curr1 is not None and curr2 is not None :
                if curr1.val == curr2.val : 
                    return dfs(curr1.right,curr2.right) and dfs(curr1.left, curr2.left)
                else : return False 
            elif curr1 is None and curr2 is None: return True
            else : return False
        return dfs(p,q) 

