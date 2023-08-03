class Stack:
    def __init__(self,lst = None)
        if lst == None:
            self.item = []
        else:
            self.item = lst

    def push(self,s):
        self.item.append(s)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]

    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)