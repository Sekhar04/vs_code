#Q1
# Create a dictionary that represents the population of five cities. Perform the following operations:
# a. Add two more cities and their populations to the dictionary.
# b. Find the city with the highest population.
# c. Check if a city "London" is present in the dictionary.
# d. Remove a city and its population from the dictionary.

pop = {"New York": 8419600,
        "Los Angeles": 3980400,
        "Chicago": 2716000,
        "Houston": 2328000,
        "Phoenix": 1690000}
pop["Philadelphia"] = 1584200
pop["San Antonio"] = 1547200
print(pop)

print("City with highest population:", max(pop, key=pop.get))
if "London" in pop:
    print("London is present in the dictionary.")
else:
    print("London is not present in the dictionary.")

del pop["Chicago"]
print("After removing Chicago:", pop)


# Create a dictionary that maps the names of students to their respective marks in an exam. Perform the following operations:
# a. Add a new student and their marks to the dictionary.
# b. Calculate the average marks of all students.
# c. Find the student with the highest marks.
# d. Sort the dictionary by student names in alphabetical order.

students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92,
    "Eve": 88
}
students["Frank"] = 95
print("Students and their marks:", students)
highest_student = max(students, key=students.get)
print("Student with highest marks:", highest_student, "with marks", students[highest_student])
average_marks = sum(students.values()) / len(students)
print("Average marks of all students:", average_marks)
sorted_students = dict(sorted(students.items()))
print("Students sorted by names:", sorted_students)

