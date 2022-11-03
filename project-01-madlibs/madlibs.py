#Extra 1: stored story in a file called "madlibs.txt" which is read in my program 
#Extra 2: added unique replacement (e.g <NAME>) which is first selected randomly but is reused. 
#
import random

madlibs_file = open("madlibs.txt","r")
if madlibs_file.mode == "r":
  contents = madlibs_file.read()

adjectives = ['beautiful','ugly','cute','silly','sparkly']
animals = ['dog','dragon','cat','unicorn','bunny']
names = ['bob','james','eren','aki','bond']
adverbs = ['quickly','eagerly','slowly','happily','groggily']
foods = ['cheese','lasagna','breadsticks','lettuce','steak']
nouns = ['can of beans','car','frog', 'rock','tree']
verbs = ['walked','crawled','bolted','ran','hopped']

split_contents = contents.split()

def test_madlibs(story):
  new_madlib = []
  random_name = random.choice(names)
  for word in split_contents:
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
    new_madlib.append(word.capitalize())
    
  new_madlib = ' '.join(new_madlib)  
  return new_madlib

print(test_madlibs(split_contents))