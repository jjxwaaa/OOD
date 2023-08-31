class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = None

        def __str__(self):
            return str(self.data)

        def setNext(self, next):
            self.next = next

class List:
    # Singly linked list ไม่มี header node with head and tail
    def __init__(self, head=None):
        if head is None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next is not None:  # locating tail & find size
                t = t.next
                self.size += 1
            self.tail = t

    def __str__(self):
        s = 'Linked data : '
        p = self.head
        while p is not None:
            s += str(p.data)+' '
            p = p.next
        return s

    def __len__(self):
        return self.size

    def append(self, data):
        """ add at the end of list"""
        p = Node(data)
        if self.head is None:  # null list
            self.head = p
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = p
        self.size += 1

    def append1(self, data):
        """ add at the end of list"""
        p = self.Node(data)
        if self.head is None:  # null list
            self.head = p
        else:
            t = self.head
            while t is not None:
                t = t.next
            t.next = p
        self.size += 1
    
    def add_first(self, data):
        """ add at first of list """
        p = self.Node(data)
        p.next = self.head
        self.head = p
        self.size += 1

    def add_first2(self, data):
        """ add at first of list """
        self.head = self.Node(data, self.head)
        self.size += 1
        if self.tail is None:
            self.tail = self.head

    def add_first3(self, data):
        p = self.Node(data)
        p.next = None if self.isEmpty() else self.head
        self.head = p
        self.size += 1

    def add_first4(self, data):
        if (self.isEmpty()):
            self.head = self.Node(data)
        else:
            temp = self.head
            self.head = Node(data)
            self.head.next = temp

    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return
        else:
            p = self.head
            while p.next is not None and p.next.data != data:
                p = p.next
        p.next = p.next.next
        self.size -= 1

    def removeHead(self):  # remove and retrun โหนดแรก

        if self.head is None:
            return
        if self.head.next is None:
            p = self.head
            self.head = None
        else:
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data

    def isEmpty(self):
        return self.size == 0

    def removeTail(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = self.head.next
            self.size -= 1
            return
        else:
            p = self.head
            while p.next.next is not None:
                p = p.next
        p.next = p.next.next
        self.size -= 1
        return p.data

    def sizes(self):
        return self.size

    def nodeAt(self, i):
        p = self.head
        for j in range(i):
            p = p.next
        return p

    def search(self, data):
        p = self.head
        while p is not None:
            if p.data == data:
                return p
            p = p.next
        return None

    def insertAfter(self, data, i):
        p = self.Node(data)
        q = self.nodeAt(i)
        p.next = q.next
        q.next = p

    def deleteAfter(self, i):
        q = self.nodeAt(i)
        q.next = q.next.next

    def deleteAfter2(self, data):
        if self.head is None:
            return
        if self.head.data == data and self.head.next is None:
            return
        p = self.head
        while p.next is not None:
            if p.data == data:
                if p.next == self.tail:
                    self.tail = p
                p.next = p.next.next
                self.size -= 1
                return
            p = p.next

    def isIn(self, data):
        p = self.head
        while p is not None:
            if p.data == data:
                return True
            p = p.next
        return False

 


# l1 = List()
# l1.append('a')
# l1.append('b')
# l1.append('c')
# l1.append('d')
# l1.append('e')
# l2 = List()
# l2.append('e')
# l2.append('d')
# l2.append('c')
# l2.append('b')
# l2.append('a')
# print("\ncase1 Content Equivalence1", l1.contentEquivalance(l2))
# # print("case1 Content Equivalence2", l1.contentEq2(l2))
# print("case1 Content Equivalence?", l1.contentEq8(l2))

# l1 = List()
# l1.append('e')
# l1.append('d')
# l1.append('c')
# l1.append('b')
# l1.append('a')
# l2 = List()
# l2.append('a')
# l2.append('b')
# l2.append('c')
# l2.append('d')
# l2.append('e')
# print("\ncase11 Content Equivalence1", l1.contentEquivalance(l2))
# # print("case1 Content Equivalence2", l1.contentEq2(l2))
# print("case11 Content Equivalence?", l1.contentEq8(l2))

# l1 = List()
# l1.append('a')
# l1.append('b')
# l1.append('c')
# l1.append('d')
# l1.append('e')
# l2 = List()
# l2.append('a')
# l2.append('b')
# l2.append('c')
# l2.append('d')
# l2.append('e')
# print("\ncase111 Content Equivalence1", l1.contentEquivalance(l2))
# # print("case1 Content Equivalence2", l1.contentEq2(l2))
# print("case111 Content Equivalence?", l1.contentEq8(l2))

# l1 = List()
# l1.append('a')
# l1.append('b')
# l1.append('c')
# l1.append('d')
# l1.append('e')
# l2 = List()
# l2.append('d')
# l2.append('d')
# l2.append('c')
# l2.append('b')
# l2.append('a')
# print("\ncase2 Content Equivalence1", l1.contentEquivalance(l2))
# # print("case1 Content Equivalence2", l1.contentEq2(l2))
# print("case2 Content Equivalence?", l1.contentEq8(l2))

# l1 = List()
# l1.append('a')
# l1.append('b')
# l1.append('c')
# l1.append('d')
# l1.append('d')
# l2 = List()
# l2.append('a')
# l2.append('b')
# l2.append('c')
# l2.append('d')
# l2.append('e')
# print("\ncase22 Content Equivalence1", l1.contentEquivalance(l2))
# # print("case1 Content Equivalence2", l1.contentEq2(l2))
# print("case22 Content Equivalence?", l1.contentEq8(l2))

# l1 = List()
# l1.append('a')
# l1.append('b')
# l1.append('c')
# l1.append('d')
# l2 = List()
# l2.append('d')
# l2.append('d')
# l2.append('c')
# l2.append('b')
# l2.append('a')
# print("\ncase3 Content Equivalence1", l1.contentEquivalance(l2))
# # print("case1 Content Equivalence2", l1.contentEq2(l2))
# print("case3 Content Equivalence?", l1.contentEq8(l2))

# l1 = List()
# l1.append('a')
# l1.append('a')
# l1.append('a')
# l1.append('a')
# l1.append('a')
# l2 = List()
# l2.append('d')
# l2.append('d')
# l2.append('c')
# l2.append('b')
# l2.append('a')
# print("\ncase4 Content Equivalence1", l1.contentEquivalance(l2))
# # print("case1 Content Equivalence2", l1.contentEq2(l2))
# print("case4 Content Equivalence?", l1.contentEq8(l2))

# l1 = List()
# l1.append('a')
# l1.append('b')
# l1.append('c')
# l1.append('d')
# l1.append('e')
# l2 = List()
# l2.append('a')
# l2.append('a')
# l2.append('a')
# l2.append('a')
# l2.append('a')
# print("\ncase5 Content Equivalence1", l1.contentEquivalance(l2))
# # print("case1 Content Equivalence2", l1.contentEq2(l2))
# print("case5 Content Equivalence?", l1.contentEq8(l2))

# l1 = List()
# l1.append('a')
# l1.append('b')
# l1.append('c')
# l1.append('d')
# l1.append('d')
# l2 = List()
# l2.append('e')
# l2.append('d')
# l2.append('c')
# l2.append('b')
# l2.append('a')
# print("\ncase6 Content Equivalence1", l1.contentEquivalance(l2))
# # print("case1 Content Equivalence2", l1.contentEq2(l2))
# print("case6 Content Equivalence?", l1.contentEq8(l2))

# l1 = List()
# l1.append('a')
# l1.append('b')
# l1.append('c')
# l1.append('d')
# l2 = List()
# l2.append('e')
# l2.append('d')
# l2.append('c')
# l2.append('b')
# l2.append('a')
# print("\ncase6 Content Equivalence1", l1.contentEquivalance(l2))
# # print("case1 Content Equivalence2", l1.contentEq2(l2))
# print("case6 Content Equivalence?", l1.contentEq8(l2))

# l1 = List()
# l1.append('a')
# l1.append('b')
# l1.append('c')
# l1.append('d')
# l1.append('e')
# l2 = List()
# l2.append('e')
# l2.append('d')
# l2.append('c')
# l2.append('b')
# print("\ncase7 Content Equivalence1", l1.contentEquivalance(l2))
# # print("case1 Content Equivalence2", l1.contentEq2(l2))
# print("case7 Content Equivalence?", l1.contentEq8(l2))
# print("l1", l1)
# print("l2", l2)

# print("\nTest deleteAfter")
# print(l1)
# l1.deleteAfter10('a')
# print(l1)
# l1.deleteAfter10('a')
# print(l1)
# l1.deleteAfter10('e')
# print(l1)
# l1.deleteAfter10('a')
# print(l1)
# l1.deleteAfter10('a')
# print(l1)
# l1.deleteAfter10('a')
# print(l1)
# l1.add_first4('z')
# print(l1)
# l1.add_first4('y')
# print(l1)
# l1.add_first4('x')

# print(l1)
# print("\nTest reverse")
# l1.append('1')
# l1.append('2')
# l1.append('3')
# print(l1)
# l1.reverse6()
# print(l1)

#l1 = List()
#l1.append1('a')
#l1.append1('b')
#l1.append1('c')
#l1.append1('d')
#l1.append1('e')
#print(l1)