import random
sample_sentence = 'Sam <VERB> the <NOUN> and then <VERB> the <NOUN> later.'
verbs = ['ate','drank','walked']
nouns = ['dog','hammer','cat','car','frog']
split_sample_sentence = sample_sentence.split()

new_madlib = []

for word in split_sample_sentence:
  if word == "<VERB>":
    word = word.replace("<VERB>", str(random.choice(verbs)))
  elif word == "<NOUN>":
    word = word.replace("<NOUN>", str(random.choice(nouns)))
  new_madlib.append(word)

new_madlib = ' '.join(new_madlib)
  
print(new_madlib)
