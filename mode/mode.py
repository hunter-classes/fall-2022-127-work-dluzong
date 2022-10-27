#findLargest(l) which takes in a list of numbers and returns the value of the smallest number

#freq(l,v) which takes a list of numbers (l) and a value (v). The function will return the frequency of v, that is, the number of times that v appears in l.
import random
def findLargest(l):
  largestNum = l[0]
  for num in l[1:]:
    if num > largestNum:
      largestNum = num
  return largestNum

print(findLargest(['1','2','3','4','6','5']))

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

  
print(freq(['1','2','2','3','4','5','5','2','6'],'2'))
    