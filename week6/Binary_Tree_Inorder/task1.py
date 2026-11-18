# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        
        def traverse(node):
            if node is None:
                return
            
            traverse(node.left)       # 1. Обходим левое поддерево
            result.append(node.val)   # 2. Забираем значение узла
            traverse(node.right)      # 3. Обходим правое поддерево
            
        traverse(root)
        return result
