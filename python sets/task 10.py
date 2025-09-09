'''Task 10: Count Unique Words

Description: Given a string, count the number of unique words using a set.

# Input
text = "hello world hello python"

# Output
# 3
'''

text = "hello world hello python"
s=text.split()
r=set(s)
length=len(r)
print(length)
