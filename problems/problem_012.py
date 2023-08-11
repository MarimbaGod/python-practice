# Complete the fizzbuzz function to return
# * The word "fizzbuzz" if number is evenly divisible by
#   by both 3 and 5
    #and statements
# * The word "fizz" if number is evenly divisible by only
#   3
    #or statements
# * The word "buzz" if number is evenly divisible by only
#   5
# * The number if it is not evenly divisible by 3 nor 5
#       else statement
# Try to combine what you have done in the last two problems
# from memory.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fizzbuzz"
    elif number % 3 == 0 and number % 5 != 0:
        return "fizz"
    elif number % 5 == 0 and number % 3 != 0:
        return "buzz"
    else:
        return number


print(fizzbuzz(15))
print(fizzbuzz(9))
print(fizzbuzz(20))
print(fizzbuzz(17))
