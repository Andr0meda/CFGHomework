
#Question 1
# I am building some very high quality chairs and need exactly
# four nails for each chair. I've written a program to calculate
# how many nails I need to buy to build these chairs.

# chairs = '15'
# nails = 4
# total_nails = chairs * nails
# message = 'I need to buy {} nails'.format(total_nails)
# print('You need to buy {} nails'.format(message))
# When I run the program it tells me that I need to buy 15151515 nails.
# This seems like a lot of nails. Is my program calculating the total
# number of nails correctly? What is the problem? How do I fix it?

#Answer
# The variable “chairs”  has a string assigned, since 15 is in quotation
# marks. We can fix the code by removing them. Also, we either need to
# change the print to:
# print(message)
# OR
# We need to change the print to:
# print('You need to buy {} nails'.format(total_nails))

chairs = 15
nails = 4
total_nails = chairs * nails
print('You need to buy {} nails.'.format(total_nails))


# Question 2
# I'm trying to run this program, but I get an error. What is the
# error telling me is wrong? How do I fix the program?
# my_name = Penelope
# my_age = 29
# message = 'My name is {} and I am {} years old'.format(my_name, my_age)
# print(message)

#Answer
# Variable “my_name” has another variable name assigned instead of a string. To make it a string we need to put “Penelope” in quotation marks, so:
# my_name = ‘Penelope’

my_name = 'Penelope'
my_age = 29
message = 'My name is {} and I am {} years old.'.format(my_name, my_age)
print(message)


#Question 3
# I have a lot of boxes of eggs in my fridge and I want to calculate
# how many omelettes I can make. Write a program to calculate this.
# Assume that a box of eggs contains six eggs and I need four eggs for
# each omelette, but I should be able to easily change these values if
# I want. The output should say something like "You can make 9 omelettes
# with 6 boxes of eggs".

egg = 1
box = 6 * egg
omelette = 4 * egg
total_boxes = 6
total_eggs = box * total_boxes
total_omelettes = int(total_eggs / omelette)
print ('You can make {} omelettes with {} boxes of eggs.'.format(total_omelettes, total_boxes))

#To change the number of boxes of eggs, change the number in the variable total_boxes.