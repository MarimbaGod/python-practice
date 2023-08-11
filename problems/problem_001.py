# Complete the minimum_value function so that returns the
# minimum of two values.
#
# If the values are the same, return either.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

# def minimum_value(value1, value2):
#     if value1>value2:
#         print(value2)
#     if value1<value2:
#         print(value1)
#     if value1 == value2:
#         print(value1)
# minimum_value(1, 5)

def minimum_value(value1, value2):
    if value1 > value2:
        print(value2)
    elif value1 < value2:
        print(value1)
    else:
        print(value1)

# minimum_value(22, 9)

#given solution
# def minimum_value(value1, value2):
#     if value1 < value2:
#         return value1
#     else:
#         return value2
