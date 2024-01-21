# 13) WAP to display/print the following pattern.
''' *
    **
    ***
    ****
    *****'''
    
row=int(input("enter the row of the triangle"))
for i in range(row+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()