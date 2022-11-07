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
         'age' : '50'}
person['age'] = person['age'] + 1
print(person)

k = person.keys()
print(k)
for item in k:
  print('person[',item,'] =',person[item])

#convert the dict_keys thing into a list:
klist = [x for x in person.keys()]
print(klist)

# pull out the values and convert to list
vlist = [x for x in person.values()]

a,b,c = yt

for k,v in person.items():
  print(k,v)

for k in person.keys():
  print(k,person[k])

s1 = {'name':'barney','id':1,'scores':[100,95,85]}
s2 = {'name':'jen','id':2,'scores':[95,85]}
s3 = {'name':'marcel','id':3,'scores':[99,76,88,82]}
s4 = {'name':'sookie','id':4,'scores':[98]}

student_list = [s1,s2,s3,s4,s5,s6]
student_dict = {}
for item in student_list:
  student_dict[item['id']] = item 

print(x fpr x in student_list if x['gender']=='f')
