""" 
Exercise: Conditional Statements
In this exercise, you will use conditional statements to categorise people based on their ages.
"""

# 1. Ask the user for their age as input and convert it to an integer.
user_age_str = input("Enter your age: ")12
# Convert the user_age_str to an integer
user_age_str = int(user_age_str)
# 2. Use conditional statements to categorise the user into one of the following categories:
# - If age is less than 18, print "You are a minor."
if user_age_str< 18:
    print("You are a minor.")
# - If age is between 18 and 65 (inclusive), print "You are an adult."
if user_age_str >= 18 and user_age_str <= 65: 
    print("Your are an adult.")
# - If age is 66 or higher, print "You are a senior citizen."
if user_age_str > 66:
    print("Your are a senior citizen. ")


""" 
Exercise: Conditional Statements
In this exercise, you will use conditional statements to check if a year is a leap year.
"""

year = 0000

if year % 4:
    print("Is a leap year.")




"""
Exercise: Loops
In this exercise, you will use a loop to print numbers up to a user-defined limit.
"""

# 1. Ask the user to enter a number as the limit and convert it to an integer.
limit_str = input("Enter a number as the limit: ")
limit = limit_str  # Convert the limit_str to an integer
limit = int(limit_str)
# 2. Use a  for loop to iterate from 1 to the user-defined limit (inclusive) and print each number.
for i in range (1,limit):
    print(i+1)
# Use a while loop to iterate from 1 to the user-defined limit (inclusive) and print each number.
# Initialise a variable to start the loop
number = 1
while number <= limit :
    print(number)
    number+=1


    #print number
    # Increment number in each iteration   
    #pass


"""
Exercise: Loop Control Statements
In this exercise, you will use a loop and loop control statements to print odd numbers.
"""

# 1. Ask the user to enter a number as the limit and convert it to an integer.
limit_str = input("Enter a number as the limit: ")
# Convert the limit_str to an integer
limit_str = int(limit_str)

# 2. Use a for loop to iterate from 1 to the user-defined limit (inclusive).
for i in range (limit+1):
    print(i)

# 3. Inside the loop, use a loop control statement to skip even numbers and print odd numbers.
# Fill in the code to achieve the goal:

for number in range(1):
    # Add code to check if number is odd and print odd numbers
    if i % 3 ==0:
        print(i)
    

    #pass


"""
Exercise: Nested Loops
In this exercise, you will use nested loops to generate a multiplication table.
"""
# 1. Ask the user for a number as the multiplier and convert it to an integer.
multiplier_str = input("Enter a number as the multiplier: ")
# Convert the multiplier_str to an integer
multiplier_str = int(multiplier_str)

# 2. Use nested loops to generate a multiplication table.
# The outer loop iterates from 10 to 1.
# The inner loop iterates the user-defined multiplier to 1.
# Fill in the code to complete the nested loops:

for number_x in range(1, 11):
    for number_y in range(1):
        # Add code to print the multiplication table
        product = number_x * number_y
        print(f"{number_x} * {number_y} = {product}")

        
        #pass
    #pass
