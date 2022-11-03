#findLargest(l) which takes in a list of numbers and returns the value of the smallest number

#freq(l,v) which takes a list of numbers (l) and a value (v). The function will return the frequency of v, that is, the number of times that v appears in l.
import datetime
import random


def findLargest(dataset):
  largestNum = dataset[0]
  for num in dataset[1:]:
    if num > largestNum:
      largestNum = num
  return largestNum


def freq(l,v):
  #n = 0
  #for num in l:
  #  if num == v:
  #    n += 1
  #return n
#applying list comprehension:
  return len([x for x in l if x == v])


def buildRandomList(size,maxvalue):
  #result = []
  #for x in range(size):
    #result.append(random.randrange(maxvalue))
  #return result
  result = [random.randrange(maxvalue) for x in range(size)]
  return result

  
def mode(dataset):
  '''
  returns a mode of the dataset, that is the value that appears most frequently

  if multiple values appear the same number of times and are most frequent, return any of them.

  ex: mode([5,4,5,6,7,8,5,4]) --> 5 since 5 appears the most
  mode([5,5,5,4,4,4,2,2,7,7,8,8,9,]) --> return 5 or 4 since both of those values appear 3 times which is the most
  
  strategy: assume first value is the mode, we can grab its frequency
  for each remaining item in the dataset: 
  count that items frequency and see if its the new mode so far
  '''
  modeSoFar = dataset[0]
  freqSoFar = dataset.count(modeSoFar)
  for item in dataset[1:]:
    #outer loop --> n 
    #Calling freq each time is n
    #if freq(dataset,item) > freqSoFar:
    if dataset.count(item) > freqSoFar:
      modeSoFar = item
      freqSoFar = dataset.count(item)
  return modeSoFar

def fastMode(dataset):
    # assume all values in dataset
    # are between 0 and 99 inclusive

    # 1. make a list of 100 slots
    # and set them all to 0
    # this will store our tallies
    
    # 2. Loop through our dataset
    # and for each item incremement
    # (add 1) to the appropriate
    # slot in the tallies list

    # 3. the index with the highest
    # value in tallies is the mode
  count = [0] * 100
  for value in dataset:
    count[value] += 1 
  countSoFar = 0
  modeSoFar = 0
  for num in range(100):
    if count[num] > countSoFar:
      countSoFar = count[num]
      modeSoFar = num
  return modeSoFar
      

def testMode(size,maxValue):
  print("Dataset Size:", size)
  dataset = buildRandomList(size,maxValue)
  #print(dataset)
  m = mode(dataset)
  print("Mode:",m)

#testFinaLargest takes less time than testMode
def testFindLargest(size,maxValue):
  print("Dataset Size:", size)
  dataset = buildRandomList(size, maxValue)
  #print(dataset)
  m = findLargest(dataset)
  print("Largest: ", m)

#testFindLargest(80000,30)
testMode(40000,30)

#testMode is slower since it includes frequency which is another function and frequency has a loop which takes up more time
  #run time analysis --done a little in 135, and a lot in 235
  