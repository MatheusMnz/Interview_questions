# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool: # type: ignore
        if not root:
            return True
            
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: # type: ignore
            # Se ambos os nós são None, são iguais
            if not p and not q:
                return True
            
            # Se um deles for None e o outro não, são diferentes
            if not p or not q:
                return False
            
            # Se os valores dos nós forem diferentes, são diferentes
            if p.val != q.val:
                return False
            
            # Recursivamente verifica as subárvores esquerda e direita
            return isSameTree(p.left, q.right) and isSameTree(p.right, q.left)

        return isSameTree(root.left, root.right)