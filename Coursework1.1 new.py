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
		
	

# there is no need to convert the inputs because they are in their suitable format
percentage_value = interest_rate / 100

#calculating the interst for the input value
inside_the_brackets = 1 + (percentage_value / number_of_times_of_interest )
brackets_with_power = inside_the_brackets ** (number_of_times_of_interest * years_of_invesment)
multipication_with_input = input_value *  brackets_with_power

print(f"\n€{input_value} invested at {interest_rate}% for {years_of_invesment} years compounded {number_of_times_of_interest} times per year is: € {multipication_with_input:.2f} ")
