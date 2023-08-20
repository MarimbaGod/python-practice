# Complete the find_indexes function which accepts two
# parameters, a list and a search term. It returns a new
# list that contains the indexes of the search term in
# the search list.
#
# Remember that indexes in Python are zero-based. That
# means the first element in the list is index 0.
#
# Examples:
#   * search_list:  [1, 2, 3, 4, 5]
#     search_term:  4
#     result:       [3]
#   * search_list:  [1, 2, 3, 4, 5]
#     search_term:  6
#     result:       []
#   * search_list:  [1, 2, 1, 2, 1]
#     search_term:  1
#     result:       [0, 2, 4]
#
# Look up the enumerate function to help you with this problem.
    #for some reason they want this. I Feel like .find() or .index() is better.
#like I could do index_num = search_list.find(search_term)
#find couldnt work because i need EVERY occurance of the search_term
#could do a .remove that occurance..


def find_indexes(search_list, search_term):
    # for num in search_list:
    index_list = []
    # for index in range(len(search_list) + 1):
    #     if (search_list[index] == search_term):
    #         index_list.append(num)
    # return index_list
    for i, elem in enumerate(search_list):
        if elem == search_list:
            index_list.append(i)
        return index_list



# Thanks Bryce
    # return [i for i, elem in enumerate(search_list) if elem == search_term]
