class Queue:
    def __init__(self,last = None):
        if lst == None:
            self.item = []
        else:
            self.item = lst 
    def enQueue(self ,s):
        self.item.append(s)

    def deQueue(self,s):
        return self.item.pop(0)

    def isEmpty(self):
        return self.item == []

    def size (self):
        return len(self.item)