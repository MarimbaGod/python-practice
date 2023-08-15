# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#

def calculate_sum(values):
    values = []
    if len(values) == 0:
        return None
    # else:
    #     return sum(values)
    # print(sum(values))
    sum = 0
    for item in values:
        sum = sum + item
    return sum


# values = [1, 2, 3, 4, 5, 6, 7]
# # calculate_sum(values)
# print(sum)
