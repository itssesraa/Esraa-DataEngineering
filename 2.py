name= 'esraa'
print("Hello " + name) 
#####################
x ,y ,z = 1, 2, 3
print(x, y, z)
#######################
city =[ 'cairo', 'alex', 'giza']
city.append('aswan') 
city.append('hurghada')
print(city)
city.insert(1, 'luxor')
print(city)
city.remove('giza')
print(city)
############
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
    
####################