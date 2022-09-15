def is_even(n):
  if n%2 == 0:
    return True
  else:
    return False

def is_even_short_version(n):
  return n%2 == 0

def is_odd(n):
  return not is_even(n)

def isRightAngle(a,b,c):
  '''
  c is the longest
  '''
def isRightAngle2(a,b,c):
  """
  any order for sides  
  """


print("even tests")
result = is_even(10)
print("Result for 10 is:", result)
result = is_even(11)
print("Result for 11 is:", result)

print("Direct call:", is_even)

print("Direct call short version:",is_even_short_version(15))
print("Direct call short version:",is_even_short_version(16))


def initialize(name):
  """
  input: a string in the form 'first last'
  return: a string in the form 'F. Last'
  """
  
def bondify(none):
  """
  input:string in the form "first last"
  return:"Last, First Last"
  """
  result = ""
  first  = name[0]

  first = first.upper()
  result = result +first = "."
  location = name.find(' ')
  last = name.;[location+1:].capitalize()
initialize("James Bond")
bondify("James Bond")
