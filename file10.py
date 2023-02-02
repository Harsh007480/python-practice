#Bank amount check or C/D program :- 
X=10000
int(input("please enter your  bank account number:-"))
print("Welcome")
a=input("what do you want \nAmount check \nCredit amount \nDebit amount\nplease enter anyone:-")

if a==('Amount check'):
    int(input("please enter your pin"))
    print(f"Your bank balance is :-{X}" )
    print("Thankyou")
elif a==('Credit amount'):
    b= int(input("Enter the amount you want to Credit:-"))
    int(input("please enter your pin"))
    print(f"great \n{b} is credit successfully completed \nYour total is:-{X+b} ")
    print("Thankyou")
elif a== ('Debit amount'):
    c=int(input("Enter the amount you want to Debit:-"))
    int(input("please enter your pin"))
    print(f"great \n{c} is debit successfully completed \nYour total is:-{X-c} ")
    print("Thankyou")
else:
    print("you enter something worng \n please enter right number\nTHANK YOU")  
i=1
while i<100:
      print(i)

      i+=1
print(i)      

    

print(" Thankyou \n Please vist aegin")
