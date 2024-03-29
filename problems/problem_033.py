# Complete the sum_of_first_n_even_numbers function which
# accepts a numerical count n and returns the sum of the
# first n even numbers
#
# If the value of the limit is less than 0, then it should
# return None
#
# Examples:
#   * -1 returns None
#   * 0 returns 0
#   * 1 returns 0+2=2
#   * 2 returns 0+2+4=6
#   * 5 returns 0+2+4+6+8+10=30
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.


#make a list   n_even_numbers = []
#append (sum + 2) = sum ) n times
#even = n +2

def sum_of_first_n_even_numbers(n):
    sum_tot = 0
    if len(n) < 0:
        return None
    for num in range(n + 1):
        sum_tot = sum_tot + (2 * num)
    return sum_tot
