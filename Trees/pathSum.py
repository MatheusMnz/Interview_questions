# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool: #type: ignore
        if not root:
            return False

        subSum = targetSum - root.val

        # Se for uma folha (nó sem filhos), verifica se o subSum é zero
        if subSum == 0 and not root.left and not root.right:
            return True
    
        # Caso contrário, verifica recursivamente as subárvores esquerda e direita
        return (self.hasPathSum(root.left, subSum) if root.left else False) or \
               (self.hasPathSum(root.right, subSum) if root.right else False)
