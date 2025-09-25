person = {
    'name': 'esraa', 'age': 20, 'city': 'cairo'}
print(person)
person['age'] = 21
print(person) 
person['jobs'] = 'developer'
print(person) 
###############
A= {"X": 1, "Y": 2, "Z": 3}
B ={"X": 4, "Y": 5, "Z": 6}
MAB={**A, **B}
print(MAB)
#############
KEYS = ['name', 'age', 'city']
VALUES = ['esraa', 20, 'cairo']
PROFILE = dict(zip(KEYS, VALUES))
print(PROFILE)
######################
for I in range(1, 6):
 print(I) 
