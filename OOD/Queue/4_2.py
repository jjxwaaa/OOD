class Queue :
    
    def __init__(self, list = None):
        if list == None :
            self.items = []
        else :
            self.items = list
        self.time = 0
        
    def Dequeue(self):
        if not self.isEmpty() : return self.items.pop(0)
        else : return -1
        
    def timeReset(self):
        self.time = 0
    
    def Enqueue(self, items):
        self.items.append(items)
        
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

    def Time(self):
        return self.time
    
    def __str__(self):
        s = str(self.items)
        return s

x = Queue()
y = Queue()
z = Queue()

def cashier():
    if y.size() + 1 < 6: 
        y.Enqueue(x.Dequeue())
    elif z.size() + 1 < 6: 
        z.Enqueue(x.Dequeue())
    if not y.isEmpty():
        y.time += 1
    if not z.isEmpty():
        z.time += 1
        
inp = [*input("Enter people : ")]
x.items = inp

for a in range(1, len(inp) + 1):
    if not y.isEmpty() and y.Time() == 3 :
        y.Dequeue()
        y.timeReset()
    if not z.isEmpty() and z.Time() == 2 :
        z.Dequeue()
        z.timeReset()
        
    cashier()
    print(a, x, y, z)