def clean(s):
    letters = []
    for l in s:
        if l.isalpha() or l==' ' or l=='\n':
            letters.append(l)
    result = "".join(letters)
    result = result.lower()
    return result 

def build_bow(data):
    counts = {}
    for word in data.split():
        counts.setdefault(word,0)
        counts[word] = counts[word]+1
        
    return counts
def remove_words(bag,word_list):
  newbag = {}
  for word in bag.keys():
    if word not in word_list:
      newbag[word] = bag[word]
      return newbag
def get_words_min_max(bag,mincount,maxcount):
  results = []
  for word in bags.keys():
    if bag[word] >= mincount and bag[word] <= maxcount:
      results.append([words,bag[word]))
    return results

#same as above but with list comprehension
def get_words_range(bag,mincount,maxcount):
  results = [[x,bag(x)] for x in bag if bag[x] >= mincount 
 \ and bag [x] ]


file = open("scandal.txt", encoding = 'utf-8')


raw_data = file.read()
data = clean(raw_data)
bag = build_bow(data)

stop_words = open(stopwords.txt)

f = open('stopwords.txt')
stop_words = []
for word in f.read().split():
  stop_words.append(word)