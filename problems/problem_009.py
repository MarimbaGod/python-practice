# Complete the is_palindrome function to check if the value in
# the word parameter is the same backward and forward.
#
# For example, the word "racecar" is a palindrome because, if
# you write it backwards, it's the same word.

# It uses the built-in function reversed and the join method
# for string objects.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.


def is_palindrome(word):
    word = input("palindrome checker: ")
    #input a word to check if its a palindrome
    letters = []
    reversed_list = []
    for char in word:
        letters.insert(0, char)
        #this accidentally reverses the letters anyway, so it throws False because
        #it accidentally reverses letters, and intentionally reverses it to create the other list
        reversed_list.append(char)
    if reversed_list[0] is letters[0]:
        print(True)
    else:
        (False)



# is_palindrome("racecar")

# def is_palindrome(word):
#     reversed_list_of_letters = reversed(word)                   # solution
#     reversed_word = "".join(reversed_list_of_letters)           # solution
#     if reversed_word == word:                                   # solution
#         return True                                             # solution
#     else:                                                       # solution
#         return False                                            # solution






#     reverse_list = reversed(letters)
#     if letters is reverse_list:
#         print(True)
#     else:
#         print(False)
#     # print(reverse_list)
#     print(reverse_list)

# is_palindrome("apple")

# # ['t', 'a', 'c', 'o', 'c', 'a', 't']
# # is_palindrome("racecar")
