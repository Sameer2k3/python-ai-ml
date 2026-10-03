import csv

name = input("Enter name: ")
age = input("Enter age: ")
city=input("Enter city: ")

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name, age,city])

print("Data added successfully!")