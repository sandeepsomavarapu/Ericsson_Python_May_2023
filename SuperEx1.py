class P:
    a=10 #12
    def __init__(self):
        self.a=12
    def m1(self):
        print('Parent instance method')
    @staticmethod
    def m3():
        print('Parent static method')

class C(P):

     a=888 #999 c=C()  c.a  super

     def m1(self):
         print('Child instance method')

     def __init__(self):
         self.a=999
         #super().__init__()
         print(self.a)#999
         print(super().a)#12
         self.m1()
         super().m1()
         super().m3()
c=C()#constructor