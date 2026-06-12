# Ask the user to enter two integers and one float. Convert them all to floats 
# and print their average.

num1 = int(input("Enter a first number here : "))
num2 = int(input("Enter a second number here : "))
num3 = float(input("Enter a third number here :"))

num1 = float(num1)
num2 = float(num2)
average = (num1+num2+num3)/3
print("Average of all three numbers is :",average)