#Solo project
#Extra 1: Have an option to translate different languages. The web site linked about has many translators specified including fudd, chef, and others.
#Extra 2: Try to tackle more advanced translations like converting parts of words rather than straight substitutions or inserting pirate phrases at appropriate points in your document. For example adding a sentence like “Shiver me timbers” or “Walk the plank” between sentences specified in input.txt

#opening file with text
f = open("input.txt","r")
story_file = f.read()
story_file = story_file.lower()
words = story_file.split()

#dictionaries for different speech
pirateDict = { "hello":"ahoy","hey":"ahoy","guys":"scurvy dogs", "friend":"matey","my":"me", "earlier":"afore","yes":"aye","food":"grub","you":"ye","your":"yer","story":"tale","the":"th'","is":"be","are":"be"} 

aussieDict = {"hello":"g'day","guys":"mates","friend":"mate","my":"may","food":"brekky","you":"ye", "yes":"nah yeah"}

#translates text to pirate speech
def pirateTranslator():
  for i in range(len(words)):
    word = words[i]
    if word in pirateDict:
      words[i] = pirateDict[words[i]]
    elif word == "<phrase>": #extra #2
      words[i] = "shiver me timbers"
  return ' '.join(words)

#translates text to australian speech
def aussieTranslator():
  for k in range(len(words)):
    word = words[k]
    if word in aussieDict:
      words[k] = aussieDict[words[k]]
    elif word == "<phrase>": #extra #2
      words[k] = "crikey"
  return ' '.join(words)
    
    
print(story_file)
print("----------------------")

#extra 1: option to translate diff languages
def translateOpt():
  opt = input('Would you like to translate to pirate or aussie?')
  if opt =='pirate':
    return pirateTranslator()
  else: 
    return aussieTranslator()
    
print(translateOpt())
