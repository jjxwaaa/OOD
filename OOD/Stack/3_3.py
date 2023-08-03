class Stack:

    def __init__(self):
        self.item = []

    def pop(self):
        return self.item.pop()
    
    def push(self, var):
        self.item.append(var)

    def peek(self):
        return self.item[-1]

    def size(self):
        return len(self.item)

    def is_empty(self):
        return True if len(self.item) == 0 else False


inp = list(input('Enter Infix : '))

s = Stack()

operator = {
    '*':2,
    '/':2,
    '^':3,
    '(':3,
    '+':1,
    '-':1,
}

print('Postfix : ', end = '')

for i in inp:
    if i in '+-*/^(':
        if not s.is_empty() and operator.get(i, -2) <= operator.get(s.peek(),- 2):
            while not s.is_empty() and s.peek() != '(' and operator[i] <= operator[s.peek()]:
                print(s.pop(), end = '')
        s.push(i)
    elif i == ')':
        while not s.is_empty() and s.peek() != '(':
            print(s.pop(), end = '')
        s.pop()
    else:
        print(i, end = '')

while s.size() != 0:
    print(s.pop(), end ='')