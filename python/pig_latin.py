import re

def translate(word_or_phrase):
  phrase = word_or_phrase.split(" ")
  result = []
  vowel = '^[aeiou]'
  consonants = '^[^aeiou]+'
  consonant_qu = '^[^aeiou]qu'
  q = '^qu'
  # print(re.search('^[aeiou]',word_or_phrase))
  for i in phrase:
    con = re.search(consonants,i)
    qu = re.search(q,i)
    con_qu = re.search(consonant_qu,i)
    if re.search(vowel,i):
      result.append(i + "ay")
    elif con_qu:
      result.append(i[con_qu.end():]+i[con_qu.start():con_qu.end()]+"ay")
    elif qu:
      result.append(i[qu.end():]+ i[qu.start():qu.end()] + "ay")
    elif con:
      result.append(i[con.end():] + i[con.start():con.end()]+ "ay")
  return " ".join(result)

# print(translate('quapple apple'))