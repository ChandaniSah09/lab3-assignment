# 12) WAP to find the LCM of 2number

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find the maximum of the two numbers
max_num = max(num1, num2)

# Initialize the LCM variable
lcm = max_num

# Check if lcm is divisible by both numbers
while (lcm % num1 != 0 or lcm % num2 != 0):
    lcm += max_num

# Print the result
print(f"The LCM of {num1} and {num2} is: {lcm}")
