#Solo project 3
#EXTRA: Use more than one data source and have your analysis compare,contrast, or correlate them.
import csv

#opens and reads CSV file (starbucks + cereal)
reader = csv.reader(open('sb-nutrition-drinks.csv'))
reader2 = csv.reader(open('cereal.csv'))

#test if file opened correctly
#for line in reader2:
#    print(line)

#starbucks data:
drink_cal = [] #make empty list for calorie nums
#takes each row in data as a line, and adds calorie value to cal list
for line in reader:
  drink_cal.append(line[1])
drink_cal.remove('Calories')
#removes non numbers from list
for item in drink_cal:
  if '-' in drink_cal:
    drink_cal.remove('-')

#cereals data
cereal_cal = []
for line in reader2:
  cereal_cal.append(line[3])
cereal_cal.remove('calories')     
#calculates the average calories in dataset
def calAvg(v):
  sum_cal = 0
  for item in v:
    sum_cal = sum_cal + int(item)
  average = sum_cal / len(v)
  return average

#analysis of datasets
print("The average number of calories in Starbucks drinks is:", calAvg(drink_cal))
print("The average number of calories in cereal brands is:", calAvg(cereal_cal))

#determining which data has greater calorie average
def compareAvg(avg1,avg2):
  if avg1 > avg2:
    return avg1
  else:
    return avg2

calDifference = calAvg(drink_cal) - calAvg(cereal_cal)

#comparison of two averages
print("\nThe greater average number of calories is:", compareAvg(calAvg(cereal_cal),calAvg(drink_cal)))
print("On average, Starbucks drinks have", calDifference, "more calories than cereal")    
  
