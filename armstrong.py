# 10) WAP to check armstrong number.


num = int(input("Enter a number: "))
num_str = str(num)
num_digits = len(num_str)

# Calculate the sum of each digit raised to the power of the number of digits
armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

# Check if the number is an Armstrong number
if armstrong_sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
    


