students=[
    {
        "roll":101,
        "name":"Rahul",
        "age":20,
        "course":"Python",
        "marks":85
    },
    {
        "roll":102,
        "name":"Neha",                                                                                          
        "age":19,
        "course":"SQL",
        "marks":92
    },
    {
        "roll":103,
        "name":"Amit",
        "age":22,
        "course":"Python",
        "marks":74
    },
    {
        "roll":104,
        "name":"Priya",
        "age":21,
        "course":"AI",
        "marks":96
    },
    {
        "roll":105,
        "name":"Rohan",
        "age":20,
        "course":"Python",
        "marks":67
    }
        ]

# print all students name
for student in students:
    print(student["name"])

# print the sum of everystudets marks

marksTotal=0
for student in students:
    marksTotal+=student["marks"]

print("total marks=",marksTotal)


# count the passed students
passing_marks=90
for student in students:
    if student["marks"]>=passing_marks:
        print(student["name"]," is passed")

# create a function to search the student by roll no.

def searchStudent(rollNumber):
    for student in students:
        if student["roll"]==rollNumber:
            print("student name is ",student["name"])


searchStudent(105)

# count stundent in each course
course={}
for student in students:
    if student["course"] not in course:
        course[student["course"]]=1
    else:
        course[student["course"]]+=1

print(course) 