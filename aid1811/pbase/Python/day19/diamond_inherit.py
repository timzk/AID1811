class A:
    def go(self):
        print("A")
class B(A):
    def go(self):
        print("B")
class C(A):
    def go(self):
        print("C")
class D(B,C):
    def go(self):
        print("D")
d = D()
d.go()