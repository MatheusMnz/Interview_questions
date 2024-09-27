class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: # type: ignore
        self.diameter = 0  # Inicializa o diâmetro com 0

        def height(node):
            if not node:
                return 0  # Se o nó for None, a altura é 0

            left_height = height(node.left)   # Calcula a altura da subárvore esquerda
            right_height = height(node.right) # Calcula a altura da subárvore direita

            # Atualiza o diâmetro com a soma das alturas esquerda e direita
            self.diameter = max(self.diameter, left_height + right_height)

            # Retorna a altura do nó atual
            return max(left_height, right_height) + 1

        height(root)  # Inicia o cálculo de altura e diâmetro
        return self.diameter  # Retorna o maior diâmetro encontrado
