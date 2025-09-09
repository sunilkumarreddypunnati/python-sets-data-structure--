'''Task 12: Set Operations Challenge (MNC Style)

Description: 
You have two sets representing skills of two candidates.
Print the skills common to both and those unique to each candidate.

# Input
candidate1 = {"Python", "SQL", "Excel"}
candidate2 = {"Python", "PowerBI", "Excel"}

# Output
# Common Skills: {'Python', 'Excel'}
# Unique to Candidate 1: {'SQL'}
# Unique to Candidate 2: {'PowerBI'}'''

candidate1 = {"Python", "SQL", "Excel"}
candidate2 = {"Python", "PowerBI", "Excel"}

print("Common Skills:",candidate1.intersection(candidate2))
print("Unique to Candidate 1:",candidate1.difference(candidate2))
print("Unique to Candidate 2:",candidate2.difference(candidate1))
