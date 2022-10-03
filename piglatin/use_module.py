import random
import piglatinify

for i in range(10):
  print(random.randrange(5,50))

test_word = "Hello"
result = piglatinify.piglatinify_v1(test_word)
print(test_word, "-->", result)

test_word = "Able"
result = piglatinify.piglatinify_v1(test_word)
print(test_word, "-->", result)

test_word = "cable."
result = piglatinify.piglatinify_v1(test_word)
print(test_word, "-->", result)

test_word = "able."
result = piglatinify.piglatinify_v1(test_word)
print(test_word, "-->", result)

test_word = "Table!"
result = piglatinify.piglatinify_v1(test_word)
print(test_word, "-->", result)
