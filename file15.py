# n=int(input("please enter the any number"))

# h=True

# for i in range(2,n):
#     if n%i==0:
#         h=False
# if h==True:
#     print(n,"is a prime number")
# else:
#     print(n, "is not a prime number")


# start=int(input("enter any number"))
# end=int(input("enter any number"))

size=5
num= int("*")
for i in range(size):

    for j in range(size - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print(num, end='')
            num += 1
        else:
            print(' ', end='')
    print()