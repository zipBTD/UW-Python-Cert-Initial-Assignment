# UW-Python-Cert-Initial-Assignment
This will help me get in the class.

# The First Problem
"Please write a program, in any language, that counts down from 100 to 0 in steps of 2,
and prints the numbers to the console or screen."

# The First Problem - ANSWER
for i in range(100, -2, -2):
    print(i)

# The First Problem - MY QUESTIONS TO SEAN
The output seems to look good. Why does Python print from from 100 to 0 in the code above?
I am shocked it doesn't output -2 at the end.


# The Second Problem 
"Write a program, in any language (incl pseudocode) that iterates the numbers from 1 to 100.
For any value divisible by 4, the program should print "Go".
For any value divisible by 5, the program should print "Figure".
For any value divisible by 4 and 5, the program should print "GoFigure"."

# The Second Problem - Pseudocode
Initiate the variable at 1
WHILE the value is less than or equal to 100:
    IF the value is divisible by 4 and 5:
        print the value and 'GoFigure'
    ELIF the value is divisible by 4:
        print the value and 'Go'
    ELIF the value is divisible by 5:
        print the value and 'Figure'
    add 1 to the value for the next iteration

# The Second Problem - ANSWER
'''
n = 1
while n <= 100:
    if n % 4 == 0 and n % 5 == 0:
        print(n, 'GoFigure')
    elif n % 4 == 0:
        print(n,'Go')
    elif n % 5 == 0:
        print(n, 'Figure')
    n = n + 1
'''

# The Second Problem - MY QUESTIONS TO SEAN
Do you think my pseudocode is good? I never had to try that before.
Do you think the professor wants the numbers printed with the associated strings?
I did that but am not sure if its wanted because it wasn't requested. Maybe I'm overthinking it, I know these are easy problems. 

# THANK YOU!!!



