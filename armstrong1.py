# 10) WAP to check armstrong number.


#its valid for 3digit number
num=int(input("enter the number:"))
temp=num
sum=0
while(num>0):
    sum=sum+(num%10)*(num%10)*(num%10)
    num=num//10
if temp==sum:
    print("IS ARMSTRONG")
else:
    print("IS NOT ARMSTRONG")