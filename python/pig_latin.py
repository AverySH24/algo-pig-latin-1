import re

def translate(word_or_phrase):
  phrase = word_or_phrase.split(" ")
  result = ""
  # print(re.search('^[aeiou]',word_or_phrase))
  for i in phrase:
    if re.search('^[aeiou]',i):
      result+= 

print(translate('apple'))