# Complete the can_skydive function so that determines if
# someone can go skydiving based on these criteria
#
# * The person must be greater than or equal to 18 years old, or
# * The person must have a signed consent form

#READ CAREFULLY. THIS SAYS OR. They can be <18 if they have the form

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

# def can_skydive(age, has_consent_form):
#     if age >= 18 and has_consent_form is True:
#         print("Thank you, you may jump")
#     else:
#         print("Sorry, maybe next time")

# print("What is your age: ")
# age = input()
# print("Did you sign the Form? ")
# has_consent_form = input()

# can_skydive(age, has_consent_form)


def can_skydive(age, has_consent_form):
    if age >= 18 or has_consent_form:                           # solution
        # return True
        print(True)                                        # solution
    else:                                                       # solution
        # return False
        print(False)                                        # solution
    # pass
