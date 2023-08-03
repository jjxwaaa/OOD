print(" ***Infix to Postfix***")

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node(None)
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value)
            cur = cur.next
        return "".join(out[::-1])

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.is_empty():
            return -1
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return -1
        removed = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return removed.value

def infix2postfix(infix):
    stack = Stack()
    postfix = Stack()
    for char in infix:
        if char.isalnum():
            postfix.push(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while stack.peek() != '(':
                postfix.push(stack.pop())
            stack.pop()
        else:
            while not stack.is_empty() and precedence(char) <= precedence(stack.peek()):
                postfix.push(stack.pop())
            stack.push(char)
    while not stack.is_empty():
        postfix.push(stack.pop())
    return postfix


def precedence(char):
    if char == '+' or char == '-':
        return 1
    elif char == '*' or char == '/':
        return 2
    elif char == '^':
        return 3
    else:
        return 0


x = input("Enter Infix expression : ")
print("Postfix :")
print(infix2postfix(x))