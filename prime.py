# 7) WAP to check prime number.

num=int(input("enter a number:"))
for i in range(2,num):
    if num%i==0:
        print("NOT PRIME NO.")
        break
else:
    print("IS PRIME NO.")