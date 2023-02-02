
'''n=5
for i in range(n):
    print(" " * (n-i-1),end="")
    print(1*(2*i+1),end="")
    print(" " * (n-i-1))

num_rows = 5
for i in range(0, num_rows):
	for j in range(0, num_rows-i-1):
		print(end=" ")
	for j in  range(0, i+1):
		print("x", end=" ")
# 	print()'''
# for row in range(7):
#     for col in range(5):
#         if col==0 or (col==4 and (row%3!=0)) or ((row%3==0)and (col>0 and col<4)):
#             print("+",end="")
#         else:
#             print(end=" ")
#     print()
# print(end="")
# for row in range(7):
#     for col in range(5):
#         if(row!=0 and (col==0 or col==4) ) or ((row==0 or row==3) and(col>1 or col<4)):
#             print("+",end="")
#         else:
#             print(end=" ")
#     print()
# print(end="")
# for row in range(7):
#      for col in range(5)

# ****
# *   *
# *   *
# ****
# this ==== B ====
# for row in range(7):
#     for col in range(5):
#         if(( col==1
#          or col==4) and row!=0 and row!=6) or ( row==0 or row==3 or row==6)and(col>0 and col<4 ):
#          print("*",end="")
#         else:
#          print(end=" ")
#     print()
# # this === A ====
# for row in range(7):
#     for col in range(5):
#         if(( col==0 or col==4) and row!=0 and row!=6) or ( row==0 or row==3)and(col>0 and col<4 ):
#          print("*",end="")
#         else:
#          print(end=" ")
#     print()

# #this ==== H ======
# for row in range (8):
#     for col in range(5):
#         if ((col==0 or col ==4) and row!=0 )or(  row==4)and(col>0 and col<4):
#            print("*",end="")
#         else:
#            print(end=" ")
#     print()

for row in range (7):
    for col in range (5):
        if ((col==0 )and  row==0 )or(row==0 or row==3 ):

            print("*",end="")
        else:
          print (end=" ")
    print()