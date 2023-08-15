# Complete the add_csv_lines function which accepts a list
# as its only parameter. Each item in the list is a
# comma-separated string of numbers. The function should
# return a new list with each entry being the corresponding
# sum of the numbers in the comma-separated string.
#
# These kinds of strings are called CSV strings, or comma-
# sepearted values strings.
#
# Examples:
#   * input:  []
#     output: []
#   * input:  ["3", "1,9"]
#     output: [3, 10]
#   * input:  ["8,1,7", "10,10,10", "1,2,3"]
#     output:  [16, 30, 6]
#
# Look up the string split function to find out how to
# split a string into pieces.

# Write out your own pseudocode to help guide you.

# input["num,bers", "conn,ected", "to,be,added"]
#
#
#
#
#
#









#
# #
# #
# def add_csv_lines(csv_lines):
#     # csv_lines = ["3,4", "1,9"]
#     result_list = []
#     # line_sum = 0               #not here because same
#     for value in csv_lines:
#         bits = value.split(",")
#         line_sum = 0
#         for bit in bits:
#             # line_sum = 0    #not here because it keeps adding them up
#             num = int(bit)
#             line_sum += num
#         result_list.append(line_sum)
#     print(result_list)

# csv_lines = ["8,1,7", "10,10,10", "1,2,3"]
# add_csv_lines(csv_lines)


# csv_lines = ["3", "1,9"]
# add_csv_lines(csv_lines)

    #     # str(csv_lines).split(',')
    #     new_lines.append(str(csv_lines).split(','))
    #     return new_lines

    # for value1, value2 in new_lines:
    #     final_lines = []
    #     final_lines.append((value1 + value2))
    # print(final_lines)
