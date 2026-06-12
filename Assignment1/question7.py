# Ask the user for a temperature in Celsius (string input). Convert it to , 
# then calculate and print temperature in Fahrenheit.

temp = input("Enter temperature in celsius here :")
temp_celsius = float(temp)
temp_fahrenheit = (temp_celsius * 9/5) + 32
print("Temperatue in Fahrenheit is :", temp_fahrenheit)
