# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def dfs(curr1,curr2):
            if curr1 is None and curr2 is None : return True
            if curr1 is not None and curr2 is not None and curr1.val == curr2.val: 
                return dfs(curr1.right,curr2.right) and dfs(curr1.left,curr2.left)
            else : return False
            
        def Same(curr1,sub):
            if curr1 is None and sub is None : return True
            if curr1 is not None and sub is not None : 
                if dfs(curr1,sub) : return True
                else : 
                    return Same(curr1.right,sub) or Same(curr1.left,sub)
            else: return False
        return Same(root,subRoot)

