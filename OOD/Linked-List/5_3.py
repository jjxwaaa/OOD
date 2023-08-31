class Node :
    def __init__(self , data , next=None) :
        self.value = data
        if next :
            self.next = next
        else :
            self.next = None
    def __str__(self) -> str :
        return f"{self.value}"
class LinkedList :
    def __init__(self , head = None):
        if head :
            self.head = head
            
        else :
            self.head = None
            

    def __str__(self) -> str:
        cur = self.head
        s = []
        while cur :
            s.append(cur.value)
            cur = cur.next
        return "->".join(s)
    def isEmpty(self) :
        return self.head == None
    
    def append(self,data) :
        if not self.head :
            self.head = data
    def size(self) :
        cur = self.head
        count = 0
        while cur :
            count += 1
            cur = cur.next
        return count




total,bokies  = input("Enter input: ").split(" ")
bokies = bokies.split(",")
l1 = LinkedList()
list_linkedlist = [l1]
found = False
for boky in bokies :
    data,nextdata = boky.split("-")
    n1 = Node(data)
    n2 = Node(nextdata)
    n1.next = n2
    for linked in list_linkedlist :
        if not found :
            if not linked.head :
                linked.append(n1)
                found = True
            else :
                cur = linked.head 
                while cur :
                    if cur.value == n2.value and cur == linked.head:
                        linked.head = n1
                        n1.next = cur
                        found = True
                        break
                    elif cur.value == n2.value :
                        n1.next = cur
                        found = True
                        break
                    elif cur.value == n1.value :
                        cur.next = n2
                        found = True
                        break
                    cur = cur.next
    if found == True :
        found = False
    else :
        l2 = LinkedList()
        l2.append(n1)
        list_linkedlist.append(l2)
list_total = list(map(str,range(1,int(total)+1)))
for linked in list_linkedlist :
    cur = linked.head
    while cur :
        try :
            list_total.remove(cur.value)
        except :
            break
        cur = cur.next
for str in list_total :
    n = Node(str)
    temp = LinkedList()
    temp.append(n)
    list_linkedlist.append(temp)

def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if int(arr[j].head.value) > int(arr[j + 1].head.value):
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            return
bubbleSort(list_linkedlist)

list_temp = list_linkedlist[:]

for linked1 in list_temp:
    if linked1 :
        if linked1.size() > 1 :
            cur1 = linked1.head
            for linked2 in list_temp :
                if linked2 and linked1 :
                    if linked2.size() > 1 and linked2 is not linked1 :
                        cur2 = linked2.head 
                        while cur2 :
                            if cur2.value == cur1.value :
                                cur2.next = cur1.next
                                if linked1 in list_linkedlist :
                                    list_linkedlist.remove(linked1)
                                break
                            cur2 = cur2.next
i = 0
for linked in list_linkedlist :
    i += 1
    print(f"{i}: {linked}")
print(f"Number of train(s): {i}")