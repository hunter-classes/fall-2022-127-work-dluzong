#findLargest(l) which takes in a list of numbers and returns the value of the smallest number

#freq(l,v) which takes a list of numbers (l) and a value (v). The function will return the frequency of v, that is, the number of times that v appears in l.
import datetime
import random


def findLargest(l):
  largestNum = l[0]
  for num in l[1:]:
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
  freqSoFar = freq(dataset, modeSoFar)
  for item in dataset[1:]:
    if freq(dataset,item) > freqSoFar:
      modeSoFar = item
      freqSoFar = freq(dataset, modeSoFar)
  return modeSoFar


def testMode(size,maxValue):
  dataset = buildRandomList(size,maxValue)
  #print(dataset)
  t = datetime.datetime.now()
  starttime = t.microsecond / 1000
  m = mode(dataset)
  end = datetime.datetime.now()
  elapsed = (end.microsecond / 1000) - starttime
  print('size:', size, 'time:',elapsed)

d = datetime.datetime.now()
print(d)