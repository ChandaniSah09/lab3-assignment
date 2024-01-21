# 3) WAP to find which no. is greater entered by user.

num1=int(input("enter a num:"))
num2=int(input("enter a num:"))
num3=int(input("enter a num:"))
if num1>num2 and num1>num3:
    print(num1,"is greater number.")
elif num2>num1 and num2>num3:
    print(num2,"is greater number.")
else:
    print(num3,"is greater number.")