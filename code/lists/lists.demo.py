s = 'this is a string'
elist = []
l1 = [22,33,15,20]
l2 = ['one', 'two', 'three']
l3 = ['one', 2, 122, 33, 'something',23]
l4 = ['one', 23, ['a','b','c'], 5, [10,11,12]]

#similar to strings in terms of certain commands
#e.g longer_string = s+s
#slice = li[3:5]

#s[5] = 'I' <-- cannot be done -- strings are immutable
#have to do this:
new_string = s[:5]+'I'+s[6:]
#on the other hand, we can change lists directly
l1[4] = 9999999

#you can change a lists eelements on a function
#but this's generally frownded upon
#since you dont retirn anything
#which can be confusing to many softwares
def change_in_place(l,index,new_value):
  l[index]= new_value
print(11)
change_in_place(l1)

#this is slightly better
def change_in_place(l,index,new_value):
  '''
  THIS CHANGES L and returns in
  '''
  l[index]= new_value
  return l

l2 = change_in_place_and_return(l1,4,321)
print (l2)
print()
print('----------------')
#this is an example of aliasing
#it can be powerful but yoi have to be careful
#make sure you are not changing any lists
#that you don't want to change
l1 = l2x 