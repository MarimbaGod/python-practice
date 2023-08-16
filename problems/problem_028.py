# Complete the remove_duplicate_letters that takes a string
# parameter "s" and returns a string with all of the
# duplicates removed.
#
# Examples:
#   * For "abc", the result is "abc"
#   * For "abcabc", the result is "abc"
#   * For "abccba", the result is "abc"
#   * For "abccbad", the result is "abcd"
#
# If the list is empty, then return the empty string.

def remove_duplicate_letters(strings):
    unique_string = ""
    for letter in strings:
        if letter not in unique_string:
            unique_string = unique_string + letter
    print(unique_string)




#typical.. Made it way more complicated than it needed to be. On the right track though

    # string_letters = []

    # for letter in strings:
    #     string_letters.append(letter)

    # unique_list = list(set(string_letters))
    # print(unique_list)
    # # for letter in strings:
    #     string_letters.append(letter)
    # letters = string_letters
    # unique = []
    # for letter in letters:
    #     if letter not in unique:
    #         unique.insert(0, letter)
    # print(unique)

strings = ["abccba"]
remove_duplicate_letters(strings)
