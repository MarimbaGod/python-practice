# Complete the is_inside_bounds function which takes an x
# coordinate and a y coordinate, and then tests each to
# make sure they're between 0 and 10, inclusive.

def is_inside_bounds(x, y):
    ex_position = 0 <= x <= 10
    why_position = 0 <= y <= 10

    if ex_position and why_position:
        return True
    else:
        return False

# x = input("x is: ")
# y = input("y is: ")
print(is_inside_bounds(x, y))
