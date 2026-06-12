#  Ask the user for:  Principal (P), Rate (R), Time (T). Convert all to float and 
# compute simple interest: SI =(P ∗R∗T)/100

principal = input("Enter your Principal Amount here :")
rate = input ("Enter your Rate of interest here :")
time = input("Enter your Time period in month here :")
principal = float(principal)
rate = float(rate)
time = float(time)
s_interest = (principal*rate*time)/100


print("Your total simple intrest :", s_interest)
