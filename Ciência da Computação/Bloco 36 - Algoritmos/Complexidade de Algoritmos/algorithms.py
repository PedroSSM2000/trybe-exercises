def contains_duplicate(numbers):
    numbers.sort() # O(n log n)
    previous_number = 'not a number';
    for number in numbers: # O(n)
        if(previous_number == number): return True
        previous_number = number

    return False

# Time complexity: O(n log n)

# Best case scenario:
# Array is already sorted and the duplicate is at the second index
# Time complexity is O(1)

# Average case scenario:
# Array is unsorted and the duplicate is at the middle index
# Time complexity is O(n log n)

# Worst case scenario:
# Array is unsorted and the duplicate is at the last index
# Time complexity is O(n log n)

##########################################################################################

#  Suppose you are writing a function for a naval battle game. Given a
#  two-dimensional array with n rows and m columns, and a pair of coordinates x
#  for rows and y for columns, the algorithm checks whether there is a ship at
#  the target coordinate. For example:

# input = [ 0 0 0 0 1
#           0 0 0 0 1
#           1 1 1 1 1
#           0 0 0 1 0 ]

# result for (0, 4) = True
# result for (1, 1) = False
