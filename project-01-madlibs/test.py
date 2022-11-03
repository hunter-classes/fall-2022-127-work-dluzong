test_str="geeksforgeeks"
s1="geeks"
s2="abcd"
 
#string split by substring
s=test_str.split(s1)
new_str=""
 
for i in s:
    if(i==""):
        new_str+=s2
    else:
        new_str+=i
 
#printing the replaced string
print(new_str)