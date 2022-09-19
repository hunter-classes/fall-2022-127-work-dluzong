#piglatin
def piglatin(word):
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
    consonant = ('B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P',
                 'Q', 'R', 'S', 'T', 'Y', 'V', 'X', 'Z')
    firstLetter = word[0]
    firstLetter = str(firstLetter)
    firstLetter = firstLetter.upper()

    if firstLetter in vowel:
        return word + "yay"

    elif firstLetter in consonant:
        lenOfWord = len(word)
        otherLetters = word[1:lenOfWord]
        firstLetter = firstLetter.lower()

        return otherLetters + firstLetter + "ay"


print(piglatin(input("What word do you want to translate to pig latin?")))


#bondify
def bondify(name):
    """
    input: a string in the form "first last"
    returns: a string in the form "Last, First Last"
    """
    loc = name.find(" ")
    return name[loc:] + ", " + name[0:loc] + " " + name[loc:]


print(bondify("james bond"))
