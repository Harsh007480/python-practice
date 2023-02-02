x=1000
int(input("please enter your bank acount number"))
print("welcome to State Bank Of India \nWhat can i help you")
a=input("What do you want\namount check\ndebit amount\ncredit amount")
if a==('amount check'):
  int(input('enter your pin'))
  print("your bank  amount is :" ,[x])
  print('Thankyou')

elif a==('debit amount'):
  b=int(input('enter the amount you want to debit'))
  int(input('enter your pin'))
  print(b,'amount  is debit successfully completed \n your total amount is',x-b)
  print('Thankyou')

elif a==('credit amount'):
    c=int(input('enter the amount you want to credit'))
    int(input('enter your pin'))
    print(c,'amount  is debit successfully completed \n your total amount is',x-c)
    print('Thankyou')

    