# https://www.youtube.com/watch?v=6gCRgIvrn7E 8m

import collections
from collections import Counter
"""
word='commando'
print(word.count('o')) 
words=['dog','cat','rat','cat','wolf','crow','cow','pig'] 
print(words.count('cat'))
sentence="dit is een hele lange zin hele over nederland duitsland en engeland"
sentence_list=sentence.split()
print(sentence_list)
sentence_dict={}
for i in sentence_list:
    sentence_dict.update({i:sentence.count(i)})
print(sentence_dict)
sorted_sentence=sorted(sentence_dict.items())   
print(" ")
print(sorted_sentence)
sorted_sentence=sorted(sentence_dict.items(), key=lambda item:item[1], reverse=True)   
print(" ")
for i,j in sorted_sentence:
    print(i,'--->',j)
print(sorted_sentence)

#sentence="dit is een hele lange zin hele over nederland duitsland en engeland"
#sentence=sentence.split()
#counter= Counter(sentence)
#print(counter.most_common(3))
"""
sentence="de koe en het schaap"
counter= Counter(sentence)

file_path=r'f:\ccc.txt'
with open(file_path,'r',encoding='utf8') as f:
    text=f.read()

text=text.split() 
counter= Counter(text)
print(counter.most_common())

print(text)
  