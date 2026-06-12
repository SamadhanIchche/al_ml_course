# Take a decimal number as input (like 45.78  ) and output its:
# • integer part - 45
# • fractional part - .78
num = float(input("Enter a number here :"))
print("interger part -",int(num))
print("fractional part -",(round(num - int(num),2)))