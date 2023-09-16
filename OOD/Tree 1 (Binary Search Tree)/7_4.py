class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setData(self, data):
        self.data = data

    def setLeft(self):
        self.left = left

    def setRight(self):
        self.right = right

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = BST._insert(self.root,data)
        return self.root
        
    def _insert(root,data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = BST._insert(root.left,data)
        else:
            root.right = BST._insert(root.right,data)
        return root
    
    def leverOrder(self):
        q = Queue()
        q.enQ(self.root)
        while q.is_empty() is not True:
            n = q.deQ()
            print (n.getData(), end = ' ')
            if n.getLeft() is not None:
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

    def BFS(self): 
        q = Queue()
        q.enqueue(self.root)
        s = "\nBreadth : "
        while not q.is_empty():
            node = q.dequeue()
            s += str(node.data) + ' '
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
        return s


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
    
print('Preorder : ', end='')
T.preOrder()
print('\nInorder : ', end='')
T.inOrder()
print('\nPostorder : ', end='')
T.postOrder()
print(T.BFS())