#Write a function to find the smallest value in a listKfind smallest in a list of items


#Write a function that returns a new list that contains all the odd items in the original list
def oddList(list):
  newList = []
  for i in list:
    if int(i) % 2 == 1: 
      newList.append(i)
  return newList

print('This function makes a new list containing the odd numbers of the original list:')
print(oddList(['1','2','3','4','5','6']))

#Write a function that takes a string and returns a new string where all the words are capitalized
def capitalWords(words):
  return words.upper()

print("This function returns the capitalized version of a string:")
print(capitalWords("This is a string"))
  

# Write a function that takes a string and returns a new string with every word that's longer than 5 character turned into upper case
#def fiveUpper(words):
  #for i in words.split():
    #if len(i) > 5:
      #i.upper()
      

#Write a function that takes a list of numbers and returns a new list with each item squared
def squareList(list):
  list2 = [ ]
  for i in list:
    numSquare = int(i) **2
    list2.append(numSquare)
  return list2

print("This function returns the square of each number in a list:")
print(squareList(['2','4','6']))

# Write a function that takes two lists of numbers and returns a new list where each item is the corresponding values of the original lists added together. Ex [1,2,3] and [10,20,30] would return the list [11,22,33]


# chapter 10 # 10, 11, 12
#12
def samList(list):
  n = 0 
  for i in list:
    n = n + 1 
    if i == "sam":
      return n
print('This function counts words in a list up to first occurrence of "sam":')
print(samList(['i', 'am', 'named', 'sam', 'slay']))
