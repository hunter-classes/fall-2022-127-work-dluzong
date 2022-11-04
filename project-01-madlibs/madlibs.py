#Extra 1: stored story in a file called "madlibs.txt"
#Extra 2: added unique replacement (e.g <NAME>) which reused. 

import random

madlibs_file = open("madlibs.txt","r") #open text file in program (extra)
if madlibs_file.mode == "r":
  contents = madlibs_file.read() #read story in text file
  
adjectives = ['beautiful','ugly','cute','silly','sparkly']
animals = ['dog','dragon','cat','unicorn','bunny']
names = ['Bob','James','Eren','Aki','Bond']
adverbs = ['quickly','eagerly','slowly','happily','groggily']
foods = ['cheese','lasagna','breadsticks','lettuce','steak']
nouns = ['can of beans','car','frog', 'rock','tree']
verbs = ['walked','crawled','bolted','ran','hopped']

split_contents = contents.split() #splits string based on space between each word

#function:
def test_madlibs(story):
  new_madlib = []
  random_name = random.choice(names) #selects one name randomly and assigns it to random_name to be used for all occurrences of <NAME> (extra)
  
  for word in split_contents: #tests each substring in the split string
    if word == "<ADJECTIVE>":
      word = word.replace("<ADJECTIVE>", random.choice(adjectives))
    elif word == "<ANIMAL>":
      word = word.replace("<ANIMAL>", random.choice(animals)) 
    elif word == "<ADVERB>":
      word = word.replace("<ADVERB>", random.choice(adverbs))
    elif word == "<FOOD>":
      word = word.replace("<FOOD>", random.choice(foods))
    elif word == "<NOUN>":
      word = word.replace("<NOUN>", random.choice(nouns))
    elif word == "<VERB>":
      word = word.replace("<VERB>", random.choice(verbs))  
    elif word == "<NAME>":
      word = word.replace("<NAME>", random_name)
    new_madlib.append(word) #adds words to empty madlib list, including replaced words
  new_madlib = ' '.join(new_madlib) #combines madlib to one string
  return new_madlib


print("Before:", contents)
print('-----------------')
print("After:", test_madlibs(split_contents))