# 11) WAP to generate fibonacci triangle

rows = int(input("Enter the number of rows for Fibonacci triangle: "))

a, b = 0, 1
for i in range(rows):
    for j in range(i + 1):
        print(a, end=" ")
        a  = b 
        b=a + b
    print()
