d = {}
#d is an empty dictionary
d[2] = 12345
d[5] = "hello"
#dictionary is *not* a list, it is just a place that holds keys i.e key 2 is associated with 12345
d['hello'] = 'world'
d['list'] = [1,2,3,4,5,6]
d [ (1,2) ] = 55
print(d)
d['list'] = 55.3
print(d)

person = {'first' : 'John',
         'last' : "Smith"
         'age' : 50}
person['age'] = person['age'] + 1
print(person)