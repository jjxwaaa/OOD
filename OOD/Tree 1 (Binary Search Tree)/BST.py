class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right

    def __str__(self):
        return str(self.data)

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setData(self,data):
        self.data = data

    def setLeft(self,left):
        self.left = left

    def setRight(self,right):
        self.right = right


class Queue:
    def __init__(self,lst = None):
        if lst is None:
            self.items = []
        else:
            self.items = lst

    def isEmpty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def deQ(self):
        result = self.items.popleft()
        return result

    def enQ(self,data):
        self.items.append(data)


class BST:
    def __init__(self, root = None):
        self.root = None if root is None else root

    def add(self,data):
        self.root = BST._add(self.root,data)

    def _add(root,data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                root.left = BST._add(root.left, data)
            else:
                root.right = BST._add(root.right, data)
            return root

    def levelOrder(self):
        q = Queue()
        q.enQ(self.root)
        while not q.isEmpty():
            n = q.deQ()
            print(n.getData(), end = ' ')
            if n.getleft() is not None:
                q.enQ(n.getLeft())
            if n.getRight() is not None:
                q.enQ(n.getRight())

    def preOrder(self):
        BST._preOrder(self.root)
    
    def _preOrder(root):
        if root is not None:
            print(root, end = ' ')
            BST._preOrder(root.getLeft())
            BST._preOrder(root.getRight())

    def inOrder(self):
        BST._inOrder(self.root)
    
    def _inOrder(root):
        if root is not None:
            BST._inOrder(root.getLeft())
            print(root, end = ' ')
            BST._inOrder(root.getRight())

    def postOrder(self):
        BST._postOrder(self.root)
    
    def _postOrder(root):
        if root is not None:
            BST._postOrder(root.getLeft())
            BST._postOrder(root.getRight())
            print(root, end = ' ')


#####################################################################################
def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return self.root
        node = self.root
        while True:
            if data < node.data:
                if node.left == None:
                    node.left = Node(data)
                    return self.root
                node = node.left
            else:
                if node.right == None:
                    node.right = Node(data)
                    return self.root
                node = node.right