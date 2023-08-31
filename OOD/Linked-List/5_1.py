class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __str__(self):
        s=""
        t=self.head
        while t!=None:
            s+=str(t.data)
            t=t.next
            if t!=None:s+="->"
        return s
    
    def isEmpty(self):
        return self.head == None
    
    def append(self,data):
        p = Node(data)
        if self.isEmpty():
            self.head = p
        else:
            t=self.head
            while t.next!=None:
                t=t.next
            t.next = p
        self.size+=1
    
    def insert(self, index, data):
        p=Node(data)
        if self.isEmpty():
            self.head = p
        elif index==0:
            p.next = self.head
            self.head = p
        else:
            t=self.head
            i = 0
            while i<index-1:
                i+=1
                t=t.next
            p.next = t.next
            t.next = p
        self.size +=1
inp=input('Enter Input : ').split(',')
ll=LinkedList()
for i in inp[0]:
    if(i!=' '):
        ll.append(i)
if(ll.isEmpty()==0):
    print('link list : ' + ll.__str__())
else:
    print('List is empty')
for i in inp[1:]:
    j=i.split(':')
    if(len(j)>1):
        ind=int(j[0])
        data=int(j[1])
        if ind<0 or ind>ll.size:
            print("Data cannot be added")
        else:
            print('index = '+str(ind)+' and data = '+str(data))
            ll.insert(ind,data)
        if(ll.isEmpty()==0):
            print('link list : ' + ll.__str__())
        else:
            print('List is empty')