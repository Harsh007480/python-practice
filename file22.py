class teacher:  # ======= This is 1st parent class ======
    def __init__(self,n,a,h):
        self.name=n
        self.age=a
        self.hight=h
class student (teacher): 
    def __init__(self, n, a, h,s,w):
       # super().__init__(n, a, h)
        self.sname=s
        self.weight=w
class college(student):
    def __init__(self,n,a,h,s,w,c):
         self.cname=c
         teacher.__init__(self,n,a,h)
         student.__init__(self,n,a,h,s,w)
    def my_col(self):
        print("===== Hello student this is multiple inheritance =====")
C1=college("Harsh kashyap",38,5.7,"Hrash kashyap","55kg","Bareilly College Bareilly")

C1.my_col()
print(C1.name)
print(C1.age)
print(C1.hight)
print(C1.sname)
print(C1.weight)
print(C1.cname)