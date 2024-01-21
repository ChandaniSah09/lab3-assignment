# 8) WAP to check palindrome number.

num = int(input("Enter a number: "))
temp = num
reverse_number = 0

while num> 0:
    digit = num % 10
    reverse_number = reverse_number * 10 + digit
    num //= 10

if temp == reverse_number:
    print(f"{temp} is a palindrome.")
else:
    print(f"{temp} is not a palindrome.")
