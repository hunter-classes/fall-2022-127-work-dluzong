s1 = "Hello World"
s2 = 'another /nstring'
#/n represents new line
s3 = """
This is a multiline string
we use the triple quotes
for those
"""
s4 = s1 + s1 #string cantenation

print(s4)
print(s1*3)
print(3*s1)

print(len(s1))
print(len("abcde"))

#isolate the world from s1
#first find the space
space_location = s1.find(" ")
#pull out from 6(one after the space) until the end
s5 = s1[space_location+:len(s1)]
#nothing after the : means go to the end 
print(s5)

#w3, pythontutor
#codingbat: practices
