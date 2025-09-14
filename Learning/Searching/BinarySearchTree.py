class Node:
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root 
    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print (root.key, end = " ")
            self.inorder(root.right)

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)
    

bst = BST()
root = None
elements = [50,30,70,20,40,60,80]

for elem in elements:
    root = bst.insert(root, elem)

print("Inorder traversal of the BST:")
bst.inorder(root)

key_to_search = 40
result = bst.search(root, key_to_search)
if result: 
    print(f"\n{key_to_search} found in the BST.")
else: 
    print(f"\n{key_to_search} not found in the BST.")

