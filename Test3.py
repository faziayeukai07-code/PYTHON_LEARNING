fruits = ["apple" , "banana" , "mango" , "orange"]
print(fruits)
print(fruits[0])
print(fruits[2])
print(fruits[3])
print(len(fruits))

#10 modify a list
cars = ["BMW" , "Toyota" , "Honda"] #cars.replace applies to strings not lists
cars[1] = "Mercedes" 
print(cars)

#Shopping List
shopping = ["bread", "milk", "eggs"]
#print(shopping.append("rice"))
shopping.append("rice")
print(shopping)

#Debugging
student_name = "Peter" 
age = "17" 
subjects = ["Math", "English", "Python"]
print("Student: " + student_name) 
#print("Next year you will be " + age + 1) # concatenate strings only : input has integer
print(type(age))
print(int(age))
print(subjects[3])