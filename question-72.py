# . Write a Python program to:
# a)	Write data into a CSV file
# b)	Read and display it


import csv
# a) Write data into a CSV file
file_name = "data.csv"
data = [["Name", "Age", "City"],
        ["Sonu", 21, "New York"],
        ["Rohan", 19, "Los Angeles"],
        ["Raju", 25, "Chicago"]]
with open(file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
# b) Read and display it
with open(file_name, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        