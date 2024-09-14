# Control Structures in Python

**Instructions:**

1. Fork this repository to your own Github account.
2. Clone the forked repository to your local machine.
3. After completing each exercise: git add, git commit, and git push to your forked repository.


## Table of Contents
1. [What are Control Structures?](#What-are-control-structures)
1. [Conditional Statements](#conditional-statements)
1. [Loops](#loops)
1. [Loop Control Statements](#loop-control-statements)
1. [Nested Loops](#nested-loops)

## What Are Control Structures?

Control structures are constructs that enable you to control **the flow** of your program's execution. They determine the order in which statements are executed based on conditions and decisions. Python provides several control structures that are fundamental to writing structured and organized code.

Let's explore them.

## Conditional Statements

**What Are Conditional Statements?**

Conditional statements are a fundamental part of programming languages and are used to **MAKE DECISIONS** in code. Conditional statements allow you to execute different blocks of code based on whether a specified condition is `True` or `False`.

1. if statements
```python
#if statements
                    if
#if statements are used to execute a block of code when a specified condition is True
#This is the structure of an if statement

if some-condition:
    #Code under here will execute when some-condition is met/True (Mind The Indentation)

```


```python
#Let's put it into practice
#Run the code below and see what you get. What's the difference between the two?

some_condition = True

if some_condition==True:
    print("It worked :)")

--------------------------------------------------------------

some_condition = True

if some_condition:
    print("It worked :)")

#Whats the difference between the two conditional statements above?

```



```python
#Let's put it into practice
#Run the code below and see what you get. What's the difference between the two?

---------------------------------------------------------------
some_condition = True

if some_condition:
    print("It worked :)")

---------------------------------------------------------------

some_condition = False

if some_condition:
    print("Did it work?, why?")


#Remember, if statements will only execute when a specified condition is met
```

**Using Operators In Conditional Statements**
```python
#Let's put it into practice again
#Run the code below and see what you get.

x = 2
y = 2

print(x == y)

#The line above is a question, asking 'is x equal to y?' The answer would be... Yes! Hence... True
#Now...


if x == y:
    print("This line executed :)")

------------------------------------------------------------------------

x = 666 
y = 777

if x == y:
    print("Did this execute? Why?")

```


```python
#Let's put it into practice again
#Run the code below and see what you get.

x = 2
y = 5

print(x != y)

#The line above is a question, asking 'x is equal not equal to y, right?' The answer would be... Yes! Hence... True
#Now...


if x != y:
    print("This line executed :)")

------------------------------------------------------------------------

x = 666 
y = 666

if x != y:
    print("Did this execute? Why?")

```

You can now try out the other operators we touched on in the basic syntax exercise :smile:

2. else statements

```python
#else statement
                else
#The else statement is used with an if statement to execute a different block of code when the condition is false
#You can look at it from this perspective: If all fails, execute the else statement

if some-condition:
    #Code here will execute if some-condition is True
else:
    #Code here will execute when the if statement condition is not met (Mind The Indentation)
```


```python
#Let's put it into practice again
#Run the code below and see what you get. What's the difference between the two?

some_condition = True

if some_condition:
    print("some_condition is True")
else:
    print("some_condition was False")

---------------------------------------------------------------------------------------

some_condition = False

if some_condition:
    print("some_condition is True")
else:
    print("some_condition was False")

#Was the code under the else statement executed? Why?
```

```python

x = "Zakumi"

y = "zakumi"

print(x==y)

----------------------------------------------------------------------------------------

if x == y:
    print("x and y are equal, condition is True")

else:
    print("x and y are not equal, condition is False)
```

3. elif statement

```python
#elif statement
                    elif
#The elif statement, short for "else if," allows you to check additional conditions after the initial if statement.
#In other words, the elif statement is used when you have more than 2 conditions to check.
#It goes inbetween the if and else statement (sometimes, depending if there is an else statement)

#Shown below are 2 blocks of code showing the Structure of an elif:

if some-condition:
    #Will execute if some-condition is True, if not...
elif some-other-condition:
    #Will execute if some-other-condition is True
else:
    #Will execute if neither of the two conditions above(some-condition and some-other-condition) are True

---------------------------------------------------------------------------------------

if some-condition:
    #Will execute if some-condition is True.Block of code will terminate here and not continue. if not...
elif some-other-condition:
    #Will execute if the some-condition is not met and some-other-condition is True. Block of code will terminate here and not continue.    
elif another:
    #Will execute if some-condition and some-other-condition are not met, and some-other-other-condition is met/True. Block of code will terminate here and not continue.
else:
    #Will execute if neither of the 3 conditions above(some-condition and some-other-condition and another) are True
```
You can have as many elif statements as the conditions you want to check for.


DO NOT:
```python
if some-condition:
    #Executes if some-condition is True. Will continue
if some-other-condition:
    #Execcutes if some-other-condition is True. Will continue
if some-other-other-condition:
    #Executes if some-other-other-condition is True. Will continue
if some-other-other-other-condition:
    #Executes if some-other-other-other-condition is True. Will continue
if some-other-other-other-other-condition:
    #Executes if some-other-other-other-other-condition is True. Will continue
    
.
.
.

#Shown above are 5 blocks of code. Compare and contrast what the difference is with the block above
#NOTE: This is not completely wrong, but let's not focus on this for now :)  
```

```python
#Let's put it into practice 
#Run the code below and see what you get. What's the difference between the two? Try find reason for using both in different scenarios. What would drive you to choosing one over the other?

x = 5
y = 100

print(x == y)

-------------------------------------------------------------------------

if x == y:
    print("x and y are equal, condition is False")
elif x != y:
    print("x and y are not equal, condition is True")
elif x < y:
    print("x is less than y, condition is True")
elif x > y:
    print("x greater than y, condition is False")
else:
    print("All the above conditions are not True(ie the conditions are not met)")    

------------------------------------------------------------------------

if x == y:
    print("x and y are equal, condition is False")
if x != y:
    print("x and y are not equal, condition is True")
if x < y:
    print("x is less than y, condition is True")
if x > y:
    print("x greater than y, condition is False")
else:
    print("All the above conditions are not True(ie the conditions are not met)")

```

```python
#Nested conditional statements
#You can nest conditional statements inside other conditionals to handle more complex conditions.

if some-condition:
    if some-other-condition:
        #Execute if both some-condition and some-other-condition are True (Mind The Indentation)
    else:
        #Executes if some-condition is True and some-other-condition is False (Mind The Indentation)
else:
    #Executes if some-condition is False
```
Conditional statements are crucial for controlling the flow of your program. They allow you to create logic that responds to specific conditions, making it possible to write dynamic and responsive code. You can use them to make decisions, validate input, handle different scenarios, and control the behaviour of your program.


**Instructions:**

1. In this exercise, you will practice using conditional statements (if, elif, else) to make decisions. 
2. Create a program that asks the user for input and provides different responses based on the input.

## Loops

**What Are Loops?**
Loops are control structures in programming that allow you to repeat a block of code multiple times. They are essential for automating repetitive tasks and processing data efficiently. Python provides two main types of loops: the `for` loop and the `while` loop. 

Let's explore them further.

```python
#for loops
                            for
#The for loop is used to iterate over a sequence, such as a list, tuple, or string. It repeats a block of code for each item in the sequence.
#The anatomy/syntax of a for loop

for some_made_up_variable in some_sequence:
    #Executes for each item in the sequence
```

```python
#Let's put it into practice
#Run the code below and see what you get.

fruits_list = ["apple", "banana", "cherry"]
for fruit in fruits_list:
    print(f"I love {fruit}s!")
#In this example, the for loop iterates through the fruits list and prints a message for each fruit.

----------------------------------------------------------------------------------
#Let's pseudocode this
#Pseudocode - A detailed yet readable description of what a computer program or algorithm should do

"""
- We have a list called `fruits_list` which has some elements in it
- For each and every element that's in the fruits_list, assign it to the variable {fruit}.
    We start with the first element
    i.e fruit = "apple" 
- print the string with the 'fruit' variable still assigned to the first element
- Now... Repeat the same process for the second element
    i.e fruit = "banana"
- Now... Repeat the same process for the third element
    i.e fruit = "cherry"
- Any more elements? No. I guess we're done -  Loop terminates
"""
```


```python
#while loops
                            while
#The while loop continues executing a block of code as long as a specified condition is met.
#The anatomy/syntax of a while loop:
while some-condition:
    #Executes as long as some-condition is met
```

```python
#Let's put it into practice
#Run the code below and see what you get

some_condition = True

while some_condition:
    print("Loop is Running")
    break
#NOTE: If you're running a loop in the fashion shown above, make sure you provide a break statements to break out of your loop when a desired condition is met.
#If you run this loop without a break statement you risk completely breaking your PC. lol, please don't.
```

```python
#Here's a more controlled way of writing a loop
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

#In this example, the while loop continues printing the value of count as long as it's less than 5.
------------------------------------------------------------------------------------------------------------------

#Let's pseudocode this
#Pseudocode - A detailed yet readable description of what a computer program or algorithm should do

"""
- We start by declaring a variable 'count' which is assigned to 0.
- We initiate our while loop by saying, while the variable 'count' is still less then 5 (0<5==True), run the following block of code
- Print the string
- Increase the variable 'count' by 1, moving it from 0 to 1

- Now... Repeat the same process

-  While the variable 'count' is still less then 5 (1<5==True), run the following block of code
- Print the string
- Increase the variable 'count' by 1, moving it from 1 to 2
.
.
.
.
.
- While the variable 'count' is still less than 5 (5<5== False),  oh?..... What is this?

The variable count is now equal to 5, the loop conditions says that as long as 'count' is less than 5 the loop should run, this means that the loop can't carry on, right?

- Loop terminates because count(5)<5 is no longer True, hence not meeting the loop's condition to continue running.
"""
```

Both for and while loops are powerful tools for iterating through data, performing calculations, and controlling program flow. It's important to be careful with loops to avoid infinite loops (infinite while loops that never exit) and to ensure that your loops have exit conditions.


**Instructions:**

1. Explore the use of loops (for and while) to control the flow of your code.
2. Write code that iterates through a sequence of numbers or elements and performs specific actions.

## Loop Control Statements

**Instructions:**

1. Learn about loop control statements such as break and continue.
2. Create code that demonstrates how to break out of a loop or skip iterations.

## Nested Loops

*What Are Nested Loops?*

Nested loops are loops that are placed inside other loops. They are a fundamental concept in programming and are often used when you need to perform a repetitive task within another repetitive task. In Python, you can nest for loops and while loops to create complex iterations. 

```python
#Nested loops
                        for
                            for
```


```python
#Nested for loops
#You can use nested for loops to iterate over MULTIPLE SEQUENCES(list, dictionary, set, etc) or create multidimensional iterations. Here's an example of a nested for loop to print a multiplication table
#Anatomy/syntax of a nested for loop:

                        for some-random-variable in some-sequence:
                            for some-other-random-variable in some-other-sequence:
                                #Do something
```

```python

#Let's start by explaining what the range function does to clear the confusion:

#The range function in Python generates a sequence of numbers. It doesn't create a traditional list or tuple but rather produces a sequence of numbers on-the-fly. The range function is commonly used in for loops to iterate over a specific range of numbers
                        for some-variable in range(start_number,stop_number_exclusive,step):
                            #Do something
------------------------------------------------------------------------------------------------------
#Let's put it into practice
#Run the code below and see what you get
#Multiplication table generator
for i in range(1, 6):
    for j in range(1, 11):
        product = i * j
        print(f"{i} * {j} = {product}")

#In this example, the outer loop iterates through the numbers 1 to 5, and for each iteration of the outer loop,
#the inner loop iterates through the numbers 1 to 10 to generate the multiplication table.


----------------------------------------------------------------------------------------------------


#Let's pseudocode this
#Pseudocode - A detailed yet readable description of what a computer program or algorithm should do

"""
## Pseudocode Explanation

Here's a simplified explanation of how the code works:

1. Start with an outer loop (variable 'i') from 1 to 5 (excluding 6).
2. Inside the outer loop, have an inner loop (variable 'j') from 1 to 10 (excluding 11).
3. Multiply 'i' and 'j' to get the product.
4. Print the product in the format "i * j = product."

The inner loop runs completely for each 'i' value, and the outer loop advances to the next 'i' value until 5 is reached.

"""

```



**Instructions:**

1. Extend your knowledge of loops by working with nested loops.
2. Solve problems that require multiple levels of iteration.

By following this order, you will build a solid foundation in control structures in Python.
Make sure to commit your changes and push them to your forked repository after completing each exercise.
Enjoy the learning experience!
