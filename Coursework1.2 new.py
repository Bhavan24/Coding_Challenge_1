print("Welcome to the Wolving compound interest calculator!!!")
print("This program calculates your potential returns when you invest with us!!!\n ")

# User inputs (loops until user enters correct inputs)
while True:
	try:
		input_value = int(input("How much would you like to invest? "))
		break
	except:
		print("Invalid input (try entering again!)\n")
		continue

while True:
	try:
		interest_rate = float(input("What is the interest rate on your account?(in %) "))
		break
	except:
		print("Invalid input (try entering again!)\n")
		continue

while True:
	try:
		years_of_invesment = int(input("How long are you planning to invest?(in years) "))
		break
	except:
		print("Invalid input (try entering again!)\n")
		continue

while True:
	try:
		number_of_times_of_interest = int(input("How many times per year? "))
		break
	except:
		print("Invalid input (try entering again!)\n")
		continue
		

principle = float(input_value)
periods = 1

print("""
Year   Period   Old Balance    Interest    New Balance
-----------------------------------------------------------""")

for year in range(1, (years_of_invesment + 1)):
	# printing the year
	print(year, end = "\n")

	for i in range(4):
		# printing the period
		print(f"        {periods:02d}", end = "       ")
		periods += 1

		# printing old balance
		print(f"€{principle:.2f}", end = "       ")

		# Calculating and printing the interest
		interest = (principle * (interest_rate / 100)) / number_of_times_of_interest
		print(f"€{interest:.2f}", end = "       ")

		# Calculating and printing the new balance
		principle = principle + interest
		print(f"€{principle:.2f}", end = "       ")

		print()



print(f"\n€{input_value} invested at {interest_rate}% for {years_of_invesment} years compounded {number_of_times_of_interest} times per year is: € {principle:.2f} ")
