import csv

# flawed example using split
# f = open("demo.csv")
# for line in f.readlines():
#     print(line)
#     line = line.strip()
#     print(line.split(","))

# Example using csv module into a list
reader = csv.reader(open("demo.csv"))
for line in reader:
    print(line)

#reader = csv.reader(open("movies.csv"))
full_data = [x f]

#using csv.DictReader to create a list of dictionaries
#reader = csv.DictReader(open("movies.csv"))