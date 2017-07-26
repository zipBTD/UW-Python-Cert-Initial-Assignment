# Please write a program, in any language, that counts down from 100 to 0 in steps of 2,
# and prints the numbers to the console or screen.

print("Problem 1")

for i in range(100, -2, -2):
    print(i)

# Write a program, in any language (incl pseudocode) that iterates the numbers from 1 to 100.
# For any value divisible by 4, the program should print "Go". For any value divisible by 5,
# the program should print "Figure". For any value divisible by 4 and 5, the program should print "GoFigure".

# Initiate the variable at 1
# WHILE the value is less than or equal to 100:
#     IF the value is divisible by 4 and 5:
#         print the value and 'GoFigure'
#     ELIF the value is divisible by 4:
#         print the value and 'Go'
#     ELIF the value is divisible by 5:
#         print the value and 'Figure'
#     add 1 to the value for the next iteration

print("Problem 2")

n = 1
while n <= 100:
    if n % 4 == 0 and n % 5 == 0:
        print(n, 'GoFigure')
    elif n % 4 == 0:
        print(n,'Go')
    elif n % 5 == 0:
        print(n, 'Figure')
    n = n + 1

