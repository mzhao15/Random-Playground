from collections import Counter

# n = 7
# m = 1

# for _ in range(n):
#     i = 0
#     cur = []
#     while i < n:
#         for _ in range(m):
#             cur.append('0')
#             i += 1
        
#         for _ in range(m):
#             cur.append('255')
#             i += 1
    
#     print(" ".join(cur))


class Employee:
    def __init__(self, name, age):
        self.name = name
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age


emp1 = Employee('Mike', 20)
print(emp1.age)
emp1.age = 30
print(emp1.age)