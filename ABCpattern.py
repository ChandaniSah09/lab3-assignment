# 15) WAP to display/print the following pattern.
'''A
   BB
   CCC
   DDDD
   EEEEE'''
   
row=int(input("enter the roe of triangle:"))
char=ord("A")
for i in range(row+1):
    chartoprint=chr(char+i-1)
    for j in range(1,i+1):
        print(chartoprint, end=" ")
    print()