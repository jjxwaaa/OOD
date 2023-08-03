class Stack:
  def __init__(self):
    self.items = []
  
  def push(self, i):
    self.items.append(i)
  
  def pop(self):
    value = self.items[-1]
    self.items.pop()
    return value

  def top(self):
    return self.items[-1]
  
  def isEmpty(self):
    return len(self.items) == 0
  
  def size(self):
    return len(self.items)
  
def dec2bin(decnum):
  s = Stack()

  while(decnum > 0):
    s.push(decnum % 2)
    decnum //= 2
  
  ans = ""
  while(not s.isEmpty()):
    ans += str(s.pop())
  
  return ans

print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))