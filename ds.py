Kim KunHa, 201900532, Computer Science Engineering

a = 16
b = 7
c = 44
d = 0
print(a % b)
print(a - b - c)
print(a + b)
print(a * b)
print(a / b)
print(a // b)
print(a + b + c)
print(a + b + c + d)

class Student:
  def __init__(self,p1,p2,p3):
    self.name = p1
    self.num = p2
    self.major = p3
  
  def displayInfo(self):
    print(self.name)
    print(self.num)
    print(self.major)
    
    
s1 = Student("Kim KunHa", 201900532, "Computer Science Engineering")
s1.displayInfo()
  
  
