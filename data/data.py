#solo project 3
#EXTRA: 

import csv

#opens and reads CSV file (starbucks)
reader = csv.reader(open('sb-nutrition-drinks.csv'))

#test if file opened correctly
#for line in reader:
#    print(line)

cal = [] #make empty list for calorie nums
#takes each row in data as a line, and adds calorie value to cal list
for line in reader:
  cal.append(line[1])
cal.remove('Calories')
#removes non numbers from list
for item in cal:
  if '-' in cal:
    cal.remove('-')

#calculates the average
def calAvg(v):
  sum_cal = 0
  for item in cal:
    sum_cal = sum_cal + int(item)
  average = sum_cal / len(cal)
  return average

print("The average number of calories in Starbucks drinks is:", calAvg(cal))
    
  
