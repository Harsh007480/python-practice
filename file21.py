# class herry:
#     def __init__(self,v,d,s): #its is Constructor

#       self.name= v
#       self.screen=d
#       self.ram=s


#     def samrtphone(self):
#         print(f"your smartphne screen size is -{self.screen} inch")
#         print(f"your smartphne ram size is-{self.ram} GB")
    


# p1=herry("vivo",6.5,128)
    
# p1.samrtphone()

# class  car:
#     def __init__(self,n,a,p):
#         self.name=n
#         self.avg=a
#         self.price=p
        
#     def my_car(self,m):
#       self.model=m
#       print("my car model is-",self.model)
#       print("my car price ",self.price)
      

# c1=car("Audi","20-km","1cr")
    
# print(c1.name)
# print(c1.avg)
# #print(c1.__price)
# c1.my_car("Q-9")

# class suv (car):  # *** This is child class ****
#       pass

# s1=suv("bmw","30km","1cr")

# s1.my_car("Q_9")
# print(s1.name)
# print(s1.avg)

class bank: # ======= This is parent class ======
    def __init__(self,l,d,c):
        self.lone=l
        self.debit=d
        self.credit=c

    def my_bank(self):
        print("your bank lone is -",self.lone)
        print("your debit amount is -",self.debit)
        print("your credit amount is -",self.credit)

class mini_bank(bank): # ====== This is a child class =======
    
    def __init__(self, l, d, c,t):
        super().__init__(l,d,c)
        self.time=t
    def mini(self):
        print("your  bank open timeing is-",self.time)
        
B2=mini_bank(20000,3500,5000,"10 am ")

B2.mini()
B2.my_bank()