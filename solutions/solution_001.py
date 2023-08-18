def translate(words, digits):
    digit_to_char = {
        "1": "",
        "2": "ABC",
        "3": "DEF",
        "4": "GHI",
        "5": "JKL",
        "6": "MNO",
        "7": "PQRS",
        "8": "TUV",
        "9": "WXYZ"
    }
​
    digit_str = str(digits)
    valid_words_count = 0
    for word in words:
        for char_index in range(len(word)):
            current_char = word[char_index]
            current_digit = digit_str[char_index]
            valid_chars = digit_to_char[current_digit]
​
            if current_char not in valid_chars:
                break
            elif char_index == len(word) - 1:
                valid_words_count += 1
​
    return valid_words_count