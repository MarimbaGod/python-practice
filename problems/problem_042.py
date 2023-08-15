# Complete the pairwise_add function which accepts two lists
# of the same size. It creates a new list and populates it
# with the sum of corresponding entries in the two lists.
#
# Examples:
#   * list1:  [1, 2, 3, 4]
#     list2:  [4, 5, 6, 7]
#     result: [5, 7, 9, 11]
#   * list1:  [100, 200, 300]

#
# Look up the zip function to help you with this problem.

# def pairwise_add(list1, list2):
#     sum_list = []
#     num_list = zip(list1, list2)

# # for values in num_list:
# for value1, value2 in zip(list1, list2):
#     sum_list.append(value1 + value2)    #instead of trying to call using the index
#     # sum_list.append(num_list[0] + num_list[0][0]) #because it doesnt work that way
# # return sum_list
# print(sum_list)

# list2 = [100, 200, 300]
# list1 = [ 10,   1, 180]
# pairwise_add(list1, list2)

# list1:  [100, 200, 300]
# list2:  [ 10,   1, 180]
# # result: [110, 201, 480]
# pairwise_add(list1, list2)
# print(sum_list)


def pairwise_add(list1, list2):
    sum_pairs = []
    for value1, value2 in zip(list1, list2):
        sum_pairs.append(value1 + value2)
    # print(sum_pairs)
    return sum_pairs


# list1 = [1, 2, 3, 4]
# list2 = [4, 5, 6, 7]
# pairwise_add(list1, list2)
