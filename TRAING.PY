LIST=[1,2,3,4,5,6,7,8,9,10]
i=0
while i <len(LIST):
    print(LIST[i])
    i += 1

i = 0

while i < 6:
    i += 1

    if i == 3:
        continue

    print(i)  
i = 0
     
while i < 6:
    i += 1

    if i == 3:
        break

    print(i)     
##################################
LIST=[1,2,3,4,5,6,7,8,9,10]
for i in LIST:
    print(i)
    
    
    ##########################
for x in LIST:
    if x ==3:
        continue
    print(x)    
##################################
# Create variables to represent one supermarket product.
# Use the following product:

# . Product code: P101
# . Product name: Milk
# . Price: 40 EGP
# . Quantity in stock: 10
# Ask the customer to enter the required quantity of Milk.
# Check the following conditions:
# . If the quantity is less than or equal to zero, display:
# Invalid quantity.
# . If the quantity is greater than the available stock, display:
# The requested quantity is not available.
# · Otherwise, display:
# The product is available.
# Example
# Available stock: 10
# Enter required quantity: 4
# The product is available. 
   
supermarket ={
    'Product code': 'P101',
    'Product name': 'milk',
    'Price': 40,
    'Quantity in stock': 10  
}
input_quantity = int(input("Enter required quantity: "))
if input_quantity <= 0:
    print("Invalid quantity.")
    
elif input_quantity > supermarket['Quantity in stock']:
    print("The requested quantity is not available.")
    
else:
    print("The product is available.")
#######################
def details(name ,age,gender):
   input(f'hello {name}, my age {age} ,my gender is {gender}' )
   
print(details('ahmed', 20, 'male'))  
########################################### 
def detalis ():
    
    print('avarable')
    
    
    
    
    
###################### 



