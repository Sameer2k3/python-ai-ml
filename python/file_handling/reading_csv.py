import csv
# write a code to read the content from a  csv file and display it
with open("students.csv" ,"r" ,) as file:
    reader=csv.reader(file)

    for row in reader:
        print(row)

# write a code to take a new record as input from the user and add it in the csv file
