#chapter 10, exercises 4 and 6
#4. Write a function called average that takes a list of numbers as a parameter and returns the average of the numbers.
def function(list):
  total = 0
  for value in list:
    total = total + value
  return total / len(list)
print(function([1,2,3]))

#6:Write a function sum_of_squares(xs) that computes the sum of the squares of the numbers in the list xs. For example, sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29:

def sum_of_squares(xs):
  total = 0
  for sum in xs:
    sum2 = sum * sum
    total = total + sum2
  return total
   
print(sum_of_squares([2,3,4]))