# Complete the can_make_pasta function to
# * Return true if the ingredients list contains
#   "flour", "eggs", and "oil"
# * Otherwise, return false
#
# The ingredients list will always contain three items.

# basically if the list of 3 things has the right answers. So make a list of the right answer
# and check to see if the list they input has the right 3 things on the list.


# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

# def can_make_pasta(pasta_attempt):
#     ingredients = ["flour", "eggs", "oil"]
#     one = input()
#     two = input()
#     three = input()
#     pasta_attempt = ["", "", ""]
# if ingredients[] == pasta_attempt[]:
#     return True
# else:
#     return False
    # ingred1 = input("First Ingredient: ")
    # ingred2 = input("Next you need: ")
    # ingred3 = input("and now: ")
    # pasta_attempt = input
    # if ingredients == pasta_attempt:
    #     return True
    # else:
    #     return False

def can_make_pasta(ingredients):
    if (                                                # solution
        "flour" in ingredients                          # solution
        and "eggs" in ingredients                       # solution
        and "oil" in ingredients                        # solution
    ):                                                  # solution
        return True                                     # solution
    else:                                               # solution
        return False                                    # solution
    # pass                                              # problem




# print(can_make_pasta(pasta_attempt))
