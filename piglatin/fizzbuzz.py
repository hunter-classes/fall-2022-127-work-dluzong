def fizzbuzz(n):
  for count in range(1,n): 
    if count %3 == 0 and count %5 == 0:
      print("fizzbuzz")
    elif count %3 ==0:
      print("fizz")  
    elif count %5 == 0:
      print("buzz") 
    else:
      print(count)

value = 20
print('fizzbuzz up to', value)
fizzbuzz(value)



def fizzbuzz2(n):
  for number in range(1,n):
    output = ""
    if number %3 == 0:
      output = output + "fizz"
    if number %5 == 0:
      output = output + "buzz"
    if output == "":
      output = str(number)
    print(output) 
  
value = 20
print('fizzbuzz up to', value)
fizzbuzz2(value)
  