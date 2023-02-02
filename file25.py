# class A:
#     def displayA(self):
#         print("Hello my name is Harsh kashyap welcome to my program A")

# class B(A):
#     def displayB(self):
#         print("Hello my name is Harsh kashyap welcome to my program B")

# class C(B):
#     def displayC(self):
#         print("Hello my name is Harsh kashyap welcome to my program C")

# C1=C()

# C1.displayA()
# C1.displayB()
# C1.displayC()

# class A1:
#     def My_class1(self):
#         print("this is a1 class ")
# class B1:
#     def My_class2(self):
#         print("this is B1 class ")
# class Z1(A1,B1):
#     def My_class3(self):
#         print("this is Z1 class ")

# O_Z=Z1()

# O_Z.My_class1()
# O_Z.My_class2()
# O_Z.My_class3()
        

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

# import qrcode 
# # img=qr.make("https://www.linkedin.com/in/harsh-kashyap-992806249")
# # img.save("My_linkdin_profile.png")
# from PIL import Image
# qr=qrcode.QRCode(version=1,
# error_correction=qrcode.constants.ERROR_CORRECT_H,
# box_size=10,border=4,
# )
# qr.add_data("https://www.linkedin.com/in/harsh-kashyap-992806249")
# qr.make(fit=True)
# img=qr.make_image(fill_color="red",back_color="black")
# img.save("my_linkdin_p.png")

f=open("file001.txt","r")
print(f.read(5))

# f=open("file001.txt","r")

# print(f.read())
