#from class 9/29/22
def piglatinify(word):
  #keep track of if the word had a capital letter
  if word[0] == word[0].upper():
    capital = True
  else:
    capital = False
  #transform to lower case
  word = word[0].lower()+word[1:]
  first = word[0]
  #turn into piglatin
  if first in "aeiou":
    result = word + 'ay'
  else: 
    result = word[1:]+first+'ay'
  #if we started with a capital letter we have to transform the result back to have a capital letter
  if capital:
    result = result.capitalize()
  return result

print("---------------------")

def piglatinify_v1(word):
  if word[-1] in ".?!":
    end_of_sentence = true
    punctuation = word[-1]
    word = word[:-1]
  else:
    end_of_sentence = False

  if word[0] == word[0].upper():
    capital = True
  else:
    capital = False

  word = word[0].lower()+word[1:]
  first = word[0]

  if first in "aeiou":
    result = word + 'ay'
  else: 
    result = word[1:]+first+'ay'

  if capital:
    result = result.capitalize()

  #test to see if we have to add punctuation on at the end
  if end_of_sentence:
    result = result + punctuation
  return result

test_word = "Hello"
result = piglatinify_v1(test_word)
print(test_word, "-->", result)

test_word = "Able"
result = piglatinify_v1(test_word)
print(test_word, "-->", result)

test_word = "cable."
result = piglatinify_v1(test_word)
print(test_word, "-->", result)

test_word = "able."
result = piglatinify_v1(test_word)
print(test_word, "-->", result)

test_word = "Table!"
result = piglatinify_v1(test_word)
print(test_word, "-->", result)