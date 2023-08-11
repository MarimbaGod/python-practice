# Complete the max_of_three function so that returns the
# maximum of three values.
#
# If two values are the same maximum value, return either of
# them.
# If the all of the values are the same, return any of them
#
# Use the >= operator for greater than or equal to

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

# def max_of_three(value1, value2, value3):
#     if value1 >= value2 >= value3:
#         print(value1)
#     elif value1 <= value2 <= value3:
#         print(value3)
#     elif value1 <= value2 >= value3:
#         print(value2)
#     elif value1 == value2 > value3:
#         print(value1)
#     elif value1 < value2 == value3:
#         print(value2)
# max_of_three(6, 2, 3)
#this doesnt work because i have no condition where
#  value1 > value2 < value3
#where value2 is < value3
def max_of_three(value1, value2, value3):
    if value1 >= value2 and value1 >= value3:
        print(value1)
    elif value2 >= value3:
        print(value2)
    else:
        print(value3)
# just using a bit of logic, with the hint to use "and" statements


max_of_three(17, 17.1, 17.02)
