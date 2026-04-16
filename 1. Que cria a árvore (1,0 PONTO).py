# • Que cria a árvore (1,0 PONTO)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        else:
            node.right = self._insert_recursive(node.right, key)
        return node
    
    def inorder_traversal(self):
        result = []
        self._inorder_helper(self.root, result)
        return result
    
    def _inorder_helper(self, node, result):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.key)
            self._inorder_helper(node.right, result)

# Exemplo de uso:
bst = BinarySearchTree()
values = [50, 30, 70, 20, 40, 60, 80]
for v in values:
    bst.insert(v)

print("Árvore em ordem crescente:", bst.inorder_traversal())
