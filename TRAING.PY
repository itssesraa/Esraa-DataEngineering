#######frist project#################
print("Hello, Enter your age: ")
# def age():
#     return int(input()*356)
# print("Your age in days is: " + age()) fales
int_age = int(input())
age_in_days = int_age * 365
print("Your age in days is: " , age_in_days)
age_in_months = int_age * 12
print("Your age in months is: " , age_in_months)
age_IN_days = int_age *24*365
print("Your age in hours is: " , age_IN_days)

#############################
###################################################################

##gussnubuer##
import random
print("🐣Welcome to the number guessing game!")
number_to_guess = random.randint(1, 10)
attempt=0
while True:
    user_guess = int(input("Enter a number between 1 and 10: "))
    attempt += 1
    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"😍Congratulations! You've guessed the number {number_to_guess} in {attempt} attempts!")
        break
    
    ##############################################
    ##pomodoro timer##
import time
minutes = int(input("Enter the number of minutes for your Pomodoro session: "))
seconds = minutes * 60
while seconds>0:
      minutes= seconds // 60
      remaining_seconds = seconds % 60
      clock = f"{minutes:02d}:{remaining_seconds:02d}"
      print(clock, end="\r")
      time.sleep(1)
      seconds -= 1
       
##################33   task   ############################################## 
task=[]
print("Welcome to the To-Do List App!")
while True:
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        new_task = input("Enter a new task: ")
        task.append(new_task)
        print("Task added successfully!")
    elif choice == '2':
        if not task:
            print("No tasks in the list.")
        else:
            print("Your Tasks:")
            if choice=='2':
                for index, task in enumerate(task, start=1):
                    print(f"{index}. {task}")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
###########################################################

print("enter number:")
number = int(input())
if number % 2 == 0:
    print("The number is even.")
else:    print("The number is odd.")       
####################################################
print("enter 3 number:")
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))
if number1 > number2 and number1 > number3: 
    print("The largest number is:", number1)
elif number2 > number1 and number2 > number3:   
    print("The largest number is:", number2)
else:    print("The largest number is:", number3)
########################################    