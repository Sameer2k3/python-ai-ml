import csv

with open("students.csv","w" ,newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["name","marks","city"])
    writer.writerow(["sam","85","delhi"])
    writer.writerow(["john","52","lknow"])