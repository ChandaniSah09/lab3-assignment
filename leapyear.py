# 19) wAP to check the leap year
year=int(input("enter the number:"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year,"is leap year")
else:
    print(year,"is not leap year")
