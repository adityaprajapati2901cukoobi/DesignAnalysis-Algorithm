class tree:
    def __init__(self,key):
        self.center=key
        self.right=None
        self.left=None

def preorder(root):
    if root:
        print(root.center)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.center)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.center)
        inorder(root.right)

if __name__=="__main__":
    root=tree(1)
    root.left=tree(12)
    root.right=tree(9)
    root.left.left=tree(5)
    root.left.right=tree(6)
    print("\n")
    preorder(root)
    print("\n")
    postorder(root)
    print("\n")
    inorder(root)
    print("\n")
