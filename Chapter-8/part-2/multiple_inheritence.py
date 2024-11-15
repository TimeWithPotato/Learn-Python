"""
---------------      --------------
|   Class     |      |  Class     |
|   A         |      |    B       |
---------------      --------------
      |                    |
      |                    |
      -----|          |-----
           ↓          ↓
           ------------
           |   Class  |
           |    C     |
           ------------
"""
class A:
    varA = "Welcome to Class A"

class B:
    varB = "Welcome to Class B"

class C(A,B):
    varC = "Welcome to Class C"

c1 = C()
print(c1.varA," ",c1.varB," ",c1.varC)