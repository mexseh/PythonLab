# class, object, inheritance and polymorphism

#class and object

print("<------CLASS & OBJECT-------->")
class first:
    x = 10
    y = 50
    def maths(self):
        print("x + y: ", self.x + self.y)
        print("y - x: ", self.y - self.x)
        print("x * y: ", self.x * self.y)
        print("x / y: ", self.x / self.y)

s = first()
s.maths()


# Inheritance and 5 types of inheritance

print("\n<------------SINGLE INHERTANCE------------->")
#----single inheritance-----
class A:
    def show(self):
        print("This is parent class A")

class B(A):
    def display(self):
        print("This is child class B")

obj = B()
obj.show()
obj.display()

#------------multiple inheritance---------------
print("\n<------------MULTIPLE INHERTANCE------------->")
class C:
    A = "Hello"
    def showC(self):
        print("Class C:",self.A)

class D:
    B = "Jain"
    def showD(self):
        print("Class D:", self.B)

class E(C, D):
    C = "University"
    def showE(self):
        print("Class E:", self.C)

obj = E()
obj.showC()
obj.showD()
obj.showE()

#---------------------multilevel inheritance------------------
print("\n<------------MULTILEVEL INHERTANCE------------->")

class F:
    def showF(self):
        print("Class F")

class G(F):
    def showG(self):
        print("Class G")

class H(G):
    def showH(self):
        print("Class H")

obj = H()
obj.showF()
obj.showG()
obj.showH() 

#---------------------Hierarchical inheritance------------------
print("\n<------------HIERARCHICAL INHERITANCE------------->")

class I:
    x = 10
    def show(self):
        print("Class I: x =", self.x)

class J(I):
    y = 5
    def showJ(self):
        total = self.x + self.y
        print("Class J: x + y =", total)

class K(I):
    z = 3
    def showK(self):
        total = self.x + self.z
        print("Class K: x + z =", total)

ob1 = J()
ob2 = K()

ob1.show()    
ob1.showJ()   
ob2.show()   
ob2.showK()   

#---------------------Hybrid inheritance------------------
print("\n<------------HYBRID INHERITANCE------------->")

class L:
    x = 10
    def showL(self):
        print("Class L: x =", self.x)

class M(L):
    y = 5
    def showM(self):
        print("Class M: y =", self.y)

class N(L):
    z = 3
    def showN(self):
        print("Class N: z =", self.z)

class O(M, N):
    def showO(self):
        total = self.x + self.y + self.z
        print("Class O: x + y + z =", total)

# object
obj = O()
obj.showL()
obj.showM()
obj.showN()
obj.showO()



#------------------POLYMORPHISM------------------
print("\n<------------POLYMORPHISM------------->")

class Add:
    a = 10
    b = 5
    def calculate(self):
        print("Add:", self.a + self.b)

class Multiply:
    a = 10
    b = 5
    def calculate(self):
        print("Multiply:", self.a * self.b)


obj1 = Add()
obj2 = Multiply()

obj1.calculate()
obj2.calculate()


