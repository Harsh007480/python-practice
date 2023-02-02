# # class India:
# #     def __init__(self,c,s) :
# #         self.capital=c
# #         self.state=s

# #     def my_country(self):
        
# #         c=input("What is you country name")
# #         print(f"my country name is:-{c} ")

# # I1=India("dehli","up")

# # I1.my_country()
# print("Welcome to my program")

# try:
#     K=int(input("enter any number"))
#     print(f"you enter {K}")
#     Z=int(input("enter any 2nd number"))
#     if Z >0:
#         raise Exception("no:- y is gretar than 0")
#     print(f"you enter{Z}")
     
#     X=K/Z

#     print(X)

# except:
#     print("this is error")
#     Exception e:
#     print("error",e)
# else:
#     print("you do very well")
# print("good job")


# f=open("file002.txt","w")

# f.write("I am Harah kashyap 002 ")

# f.close

f=open("file001.txt","r")
print(f.read(5))
print(f.readline())
