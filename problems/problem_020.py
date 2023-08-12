# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.

def has_quorum(attendees_list, members_list):
    if len(attendees_list) >= (len(members_list) // 2):
        print(True)
    else:
        print(False)




attendees_list = ["Philip", "Gloria"]
members_list = ["Jason", "Gloria", "McDougal", "Glory", "Gloria"]
has_quorum(attendees_list, members_list)
