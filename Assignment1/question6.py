# Write a program to swap values of two numbers entered by the user
num1 = int(input("Enter the first number here :"))
num2 = int(input("enter the second number here :"))
print("Before swapping : num1 =", num1, "and num2 =", num2)
num1, num2 = num2, num1
print("After swapping : num1 =", num1, "and num2 =", num2)