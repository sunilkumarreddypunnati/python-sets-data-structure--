'''Task 11: Remove Duplicates from List

Description: Given a list, remove duplicates using a set and 
print in sorted order.

# Input
numbers = [5, 3, 1, 2, 2, 3, 4]

# Output
# [1, 2, 3, 4, 5]'''
numbers = [5, 3, 1, 2, 2, 3, 4]
s=set(numbers)
print(sorted(s))