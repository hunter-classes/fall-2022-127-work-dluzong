#7: Write a function called is_even(n) that takes an integer as an argument and returns True if the argument is an even number and False if it is odd.
def is_even(n):
  if n%2== 0:
    return True
  else:
    return False
result = is_even(4)
print("the result for 4 is", result)
result = is_even(7)
print("the result for 7 is",result)

#8: Now write the function is_odd(n) that returns True when n is odd and False otherwise.
def is_odd(n):
  if n%2 == 0:
    return False
  else: 
    return True
result = is_odd(4)
print("the result for 4 is", result)
result = is_odd(7)
print("the result for 7 is",result)

#10: Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the triangle is right-angled. Assume that the third argument to the function is always the longest side. It will return True if the triangle is right-angled, or False otherwise.
def is_rightangled(a,b,c):
  """
  c is the longest side
  """
  return a*a + b*b == c*c

print(is_rightangled(3,4,5))
print(is_rightangled(5,4,3))

#11: Extend the above program so that the sides can be given to the function in any order.
def is_rightangled2(a,b,c):
  """
  any sides
  """
  return is_rightangled(a,b,c) or \
            is_rightangled(b,c,a) or \
            is_rightangled(a,c,b)
print(is_rightangled2(5,3,4))

#Coding Bat, Strings-1
#hello_name
def hello_name(name):
  return "Hello" + " " + name + "!"

print(hello_name('Bob'))

#make_out_word
def make_out_word(out, word):
  first = out[0:2]
  second = out[2:4]
  return first + word + second

print(make_out_word('<<>>','yay')

#first_two
def first_two(str):
  if str > 2:
    return str[0:2]
  else:
    return str
    
first_two('kitten')

