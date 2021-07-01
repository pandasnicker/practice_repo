# Demo of classes and objects in Python

class A():
    def funcA(self):
        print('In the A class')

class B():
    
    def funcB(self):
        print('In the B class')


class C(B,A):
    def funcC(self):
        print('In the C class')

if __name__ == '__main__':
    baseobj = C()
    baseobj.funcC()
    print(C.__mro__) 