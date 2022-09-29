#piglatin
#TO-DO:
#1. make it work for capitalized words
  #ex: Cable -> Ablecay
#2. Handle periods (and possible other punctuation)
  #ex: Able. --> Able.ay and cable. --> ablecay.
def piglatinify(word):
    """
input: a string representing a word
returns: a new string with the word converted to piglatin

Rules:
if the first letter is a consonent, move it from the start to the end and add "ay"
so "hello" becomes "ellohay"

If the first letter is a vowel, just add "yay" to the end

try to also handle upper case words

"""
    vowel = ('A', 'E', 'I', 'O', 'U')
  #can also do if first == "A" or first == 'E' or ... 
  #even better: if first in 'aeiou'
    consonant = ('B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P','Q', 'R', 'S', 'T', 'Y', 'V', 'X', 'Z')
    firstLetter = word[0]
    firstLetter = str(firstLetter)
    firstLetter = firstLetter.upper()
    
    if firstLetter in vowel:
    #if firstLetter in 'aeiou':
      result = word.capitalize() + "yay"

    elif firstLetter in consonant:
        lenOfWord = len(word)
        otherLetters = word[2:lenOfWord]
        firstLetter = firstLetter.lower()
        secondLetter = word[1]
        secondLetter = secondLetter.upper()
        result = secondLetter + otherLetters + firstLetter + "ay"
        # or result = word[1:]+first+'ay'
    
    for punctuation in (".,?!"):
      if punctuation in word:
        punc = result.find(punctuation)
        result = result[0:punc] + result[punc+1:] + result[punc]
  
    return result

test_word = "Hello"
result = piglatinify(test_word)
print(test_word, "-->", result)

test_word = "Able"
result = piglatinify(test_word)
print(test_word, "-->", result)

test_word = "cable."
result = piglatinify(test_word)
print(test_word, "-->", result)

test_word = "able."
result = piglatinify(test_word)
print(test_word, "-->", result)

#bondify
def bondify(name):
    """
    input: a string in the form "first last"
    returns: a string in the form "Last, First Last"
    """
    loc = name.find(" ")
    return name[loc:] + ", " + name[0:loc] + " " + name[loc:]


print(bondify("james bond"))
