import random

sample_sentence ='''
Today there was a <ADJECTIVE> <ANIMAL> who <ADVERB> woke up very hungry.

They had an appetite for <FOOD> and searched and searched, eventually finding it behind a <NOUN> and ate it.

When they were finished, they <VERB> back home.
'''


adjectives = ['beautiful','ugly','cute','silly','sparkly']
animals = ['dog','dragon','cat','unicorn','bunny']
adverbs = ['quickly','eagerly','slowly','happily','groggily']
foods = ['cheese','lasagna','breadsticks','lettuce','steak']
nouns = ['can of beans','car','frog', 'rock','tree']
verbs = ['walked','crawled','bolted','ran','hopped']

split_sample_sentence = sample_sentence.split()

x = 0
while x < 2:
  new_madlib = []
  for word in split_sample_sentence:
    if word == "<ADJECTIVE>":
      word = word.replace("<ADJECTIVE>", str(random.choice(adjectives)))
    elif word == "<ANIMAL>":
      word = word.replace("<ANIMAL>", str(random.choice(animals)))
    elif word == "<ADVERB>":
      word = word.replace("<ADVERB>", str(random.choice(adverbs)))
    elif word == "<FOOD>":
      word = word.replace("<FOOD>", str(random.choice(foods)))
    elif word == "<NOUN>":
      word = word.replace("<NOUN>", str(random.choice(nouns)))
    elif word == "<VERB>":
      word = word.replace("<VERB>", str(random.choice(verbs)))           
    new_madlib.append(word)
  new_madlib = ' '.join(new_madlib)  
  print(new_madlib)
  print(' ')
  x = x+1
