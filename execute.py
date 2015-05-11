"""
try:
	pay = float(input("What is your hourly wage?: "))
	hours = float(input("How many hours did you work? "))
	net_pay = pay * hours
	print ("Your pay for this week is: $" + str(net_pay))
except:
	print("Please enter numerica values")
"""

"""
hrs = raw_input("Enter Hours: ")
h = float(hrs)
rate = raw_input("Enter your wage: ")
r = float(rate)

if h <= 40:
    print h * r
else:
    print (r * 40 + (r * 1.5 * (h - 40)))
"""

def computepay(h, r):
    if h <= 40: 
        p = r * h
    else:
        p = r * 40 + (r * 1.5 * (h - 40))
    return p

total_pay = computepay(float(raw_input("Enter Hours: ")), float(raw_input("Enter hourly wage: ")))

print total_pay
