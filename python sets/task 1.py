'''Task 1: Create & Print Unique Elements

Description: Given a list, create a set and 
print all unique elements in ascending order.

# Input
numbers = [4, 2, 2, 3, 1, 4]

# Output
# {1, 2, 3, 4}'''

numbers = [4, 2, 2, 3, 1, 4]
s=set(numbers)
unique=sorted(s)
print("{" + ", ".join(map(str, unique)) + "}")
