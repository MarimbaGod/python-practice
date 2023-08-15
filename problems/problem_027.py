# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#

def max_in_list(values):
    # values = [2, 4, 1, 3, 7, 6, 9]
    if len(values) == 0:
        return None
    highest_num = values[0]

    for num in values:
        if num >= highest_num:
            highest_num = num
    return highest_num
    print(highest_num)
# print(highest_num)


values = [2, -4, 1, 32, 71, 6, 93]
print(max_in_list(values))



    # test_num = 0               #closest attempt out of both tries
    # for num in values:
    #     test_num =+ num
    # if


#this didnt work because .remove() does not change the index positions
#         if values[0] >= values[1]:
#             values.remove(values[1])
#             # return values[0]
#         elif values[0] <= values[1]:
#             values.remove(values[0])
#         else:
#             values.remove(values[1])
#     print(values)

# values = [7, 6, 9]
