print("mini calculater")

num1=float(input("enter first number here:"))
num2=float(input("enter second number here:"))
print("press1 for addition\npress2 for substraction\npress3 for multiplication\npress4 for division\npress5 for exponention")

choice=int(input("enter  choice from 1-5"))
if choice==1:
  print(num1+num2)
elif choice==2:
  print(num1-num2)
elif choice==3:
  print(num1*num2)
elif choice==4:
  print(num1/num2)
elif choice==5:
  print(num1**num2)
else:
  print("enter invalid number ")