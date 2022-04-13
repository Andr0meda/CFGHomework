# Question 1
# This for loop creates the variable "output", multiplies all numbers from
# zero to 99 with the character "o" and pints each result on the screen. The result
# starts with a blank for 'o' * 0 and continues with printing one 'o', then two etc.
# until 99 'o' characters and then it stops.
for number in range(100):
    output = 'o' * number
    print(output)


# Question 2
# We need to add the "return" statement so that the program keeps running and send
# the result back to us.
# Also, adding int converts the output into integer (without int we get 120.0).
def calculate_vat(amount):
   return int(amount * 1.2)
total = calculate_vat(100)
print(total)







