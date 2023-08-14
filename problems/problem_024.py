# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#basic sum() function // 2

# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you



#I forgot to return none if the list is empty.
#I already saw the answer though, so its just basically
#checking to see if the len of the list == 0, and if it does,
#return None

def calculate_average(values):
    values = [10, 2, 8, 1, 61]
    for num in values:
        # sum_total = 0
        # sum_total = (sum_total + num)
        average_num = int(sum(values)) // 2
    # average = sum_total // 2
    print(average_num)
values = [10, 2, 8, 1, 61]
calculate_average(values)

#not sure if this can survive really stress testing. It doesnt seem too functional.
#dont know why i need to input the list twice.
#this is why I like the input prompts



#     for num in values:
#         values = [1, 2, 3, 4, 5]
#         sum = 0
#     sum = sum + num

# average = (sum) // 2

# print(average)

# values = [1, 2, 3, 4, 5]
# calculate_average(values)
