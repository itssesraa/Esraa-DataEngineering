#Lists
#1. Create a list of 5 student names and print the list.

students =['esraa','nour','ahmed','mohamed','ali']
print(students)

#2. Add a new student to the list and print the updated list.
students.append('sara')
print(students)

#3. Sort the list alphabetically and print it.
students.sort()
print(students)

#Dictionaries

#4. Create a dictionary with keys: 'name', 'age', and 'grade'. Assign them any values
student_info = {
    'name': 'esraa',
    'age': 20,
    'grade': 'A'
}
print(student_info)
#5. Add a new key to the dictionary: 'subject' with a value of your choice.

student_info['subject'] = 'Math'
print(student_info)
#6. Print all the keys and values in the dictionary using a loop.
for key, value in student_info.items():
    print('Key:', key, 'Value:', value)
    
#########################
# Arrays with NumPy
#7. Import NumPy and create a 1D array with values from 1 to 10.

import numpy as np
array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(array_1d)

#8. Reshape it into a 2D array with 2 rows and 5 columns.
array_2d = array_1d.reshape(2, 5)
print(array_2d)

#9. Calculate and print the mean, median, and standard deviation of the array.
mean_value = np.mean(array_1d)
median_value = np.median(array_1d)
std_deviation = np.std(array_1d)
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_deviation)

#0. Accessing and Slicing: Print only the first row of the 2D array and the third element from the second row.
print("First row of 2D array:", array_2d[0])
print("Third element from the second row:", array_2d[1, 2])
#🧩 PART 4: DataFrames with pandas (10 Tasks)
#11. Create a list of dictionaries with the following data of 5 students:
import pandas as pd

students = [
{'name': 'Ali', 'age': 18, 'grade': 85},
{'name': 'Sara', 'age': 19, 'grade': 90},
{'name': 'Laila', 'age': 17, 'grade': 75},
{'name': 'Omar', 'age': 18, 'grade': 88},
{'name': 'Huda', 'age': 20, 'grade': 92}
]

#12. Create a pandas DataFrame from the list.
df_students = pd.DataFrame(students)
print(df_students)
#13. Display the first 3 rows of the DataFrame.
print(df_students.head(3))
#14. Add a new column 'status' that shows 'Pass' if grade ≥ 80, else 'Fail'.
df_students['status'] = df_students['grade'].apply(lambda x: 'Pass' if x >= 80 else 'Fail')
print(df_students)
#15. Filter and print only the students who passed.
passed_students = df_students[df_students['status'] == 'Pass']
print(passed_students)  
#16. Sort the DataFrame by grade in descending order and display it.
sorted_students = df_students.sort_values(by='grade', ascending=False)
print(sorted_students)
#17. Access a specific column: Print only the 'name' column.
print("Names of students:")
print(df_students['name'])

#18. Access a specific row: Print the details of the student in index position 2.
print("Details of student at index 2:")
print(df_students.iloc[2])
#19. Filter multiple conditions: Show students who are older than 18 and scored more than 85
filtered_students = df_students[(df_students['age'] > 18) & (df_students['grade'] > 85)]
print("Students older than 18 and scored more than 85:")
print(filtered_students)


#20. Slice the DataFrame: Print the first two rows using slicing.
filtered_students = df_students[(df_students['age'] > 18) & (df_students['grade'] > 85)]
print("Students older than 18 and scored more than 85:")
print(filtered_students)
print("First two rows of the DataFrame:")   
print(df_students.head(2))