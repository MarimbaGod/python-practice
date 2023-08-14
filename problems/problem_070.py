# Write a class that meets these requirements.
#
# Name:       Book
#
# Required state:
#    * author name, a string
#    * title, a string
#
# Behavior:
#    * get_author: should return "Author: «author name»"
#    * get_title:  should return "Title: «title»"
#
# Example:
#    book = Book("Natalie Zina Walschots", "Hench")
#
#    print(book.get_author())  # prints "Author: Natalie Zina Walschots"
#    print(book.get_title())   # prints "Title: Hench"
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

class Book:
    def __init__(self, author_name, title):
        self.author_name = author_name
        self.title = title

    # def get_author(self, author_name): #Only need to include
    # function_name(self): one parameter - (self)
    #but idk why
    def get_author(self):
        # return "Author :" + author_name
        return "Author: " + self.author_name

    # def get_title(self, title):
    def get_title(self):
        # return "Title: " + title # NEED THE self.value_name
        return "Title: " + self.title


#test Example
book = Book("Sarah J. Maas", "Court of Wings and Ruin")

print(book.get_author())  # prints "Author: Sarah J. Maas"
print(book.get_title())   # prints "Title: Court of Wings and Ruin"
