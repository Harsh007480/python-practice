#Calculater program made by Me
print("Welcome my calculater")

a=int(input("enter any 1st number"))
b=int(input("enter any 2nd number"))
z=input("enter any operator")

if z == ("+")  :
    print(a+b)
    print(f"your addtion is : {a+b}")

elif  z == ('-')   :
    print(a-b) 
    print(f"your subtraction is : {a-b}")
elif  z == ('*')   :
    print(a*b) 
    print(f"your multiplication is : {a*b}")
elif  z == ('/')   :
    print(a/b) 
    print(f"your division is : {a/b}")
else:
    print("you enter worng operator")
    print("plase enter right operator : + , - , * , / etc")


print("exit")