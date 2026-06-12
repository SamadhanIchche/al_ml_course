'''The user enters a string containing a number (e.g."45" ). 
Convert it to:
• an integer
• a float
• a string again
Print all three values with their types.'''

num = input ("Enter a number here :")
num_int = int(num)
num_float = float(num)
num_str = str(num)
print(num_int, type(num_int))
print(num_float, type(num_float))
print(num_str, type(num_str))
