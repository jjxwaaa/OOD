class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        newNode = Node(item)
        newNode.next = None
        if self.head == None:
            newNode.previous = None
            self.head = self.tail = newNode
            self.size += 1
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = newNode
            self.tail = newNode
            newNode.previous = p
            self.size += 1

    def addHead(self, item):
        newNode = Node(item)
        newNode.next = self.head
        if self.head != None:
            self.head.previous = newNode
        self.head = newNode
        p = self.head
        while p.next != None:
            p = p.next
        self.tail = p
        self.size += 1

    def insert(self, pos, item):
        newNoode = Node(item)
        if pos == 0 or pos <= 0-self.size:
            self.addHead(item)
            
        if pos >= self.size:
            self.append(item)
            
        elif pos > 0 and pos <= self.size:
            p = self.head
            for i in range(self.size):
                if i == pos:
                   q = p.previous
                   break
                p = p.next
            q.next = newNoode
            newNoode.previous = q
            newNoode.next = p
            newNoode.next.previous = newNoode
            self.size += 1
        elif pos < 0 and pos > 0-self.size:
            PosPositia = pos + self.size
            p = self.head
            for i in range(self.size):
                if i == PosPositia:
                   q = p.previous
                   break
                p = p.next
            q.next = newNoode
            newNoode.previous = q
            newNoode.next = p
            newNoode.next.previous = newNoode
            self.size += 1
       
    def search(self, item):
        p = self.head
        for i in range(self.size):
            if p.value == item:
                return 'Found'
            p = p.next
        return 'Not Found'

    def index(self, item):
        q = self.head
        for i in range(self.size):
            if q.value == item:
                return i
            q = q.next
        return -1

    def size(self):
        x = self.size
        return str(x)

    def pop(self, pos):
        if pos < 0 or pos >= self.size:
            return 'Out of Range'
        if pos == 0 and self.size > 0:
            self.head = self.head.next
            self.size -= 1
            return 'Success'
        else:
            p = self.head
            for i in range(0,pos-1):
                p = p.next
            p.next = p.next.next
            self.size -= 1
            return 'Success'

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
        
    elif i[:2] == "AH":
        L.addHead(i[3:])
        
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
     
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size, L))
       
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
       
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
       
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
       
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())