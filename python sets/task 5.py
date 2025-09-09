'''Task 5: Symmetric Difference

Description: Find elements in either set but not in both.

# Input
a = {1, 2, 3}
b = {3, 4, 5}

# Output
# {1, 2, 4, 5}'''

a = {1, 2, 3}
b = {3, 4, 5}
result=a.symmetric_difference(b)
print(result)