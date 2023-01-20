from nltk.corpus import wordnet, sentiwordnet as swn

import pandas
word = "present"

info_word = wordnet.synsets(word)
#print (info_word)

print(info_word[0].lexname())
print(info_word[0].definition())

print(info_word[1].lexname())
print(info_word[1].definition())

print(info_word[2].lexname())
print(info_word[2].definition())

tree = wordnet.synset('tree.n.01')
dog = wordnet.synset('dog.n.01')
cat = wordnet.synset('cat.n.01')
bird = wordnet.synset('bird.n.01')
tiger = wordnet.synset('tiger.n.01')

words = [tree, dog, cat, bird, tiger]
similarities = []
words_name = [i.name().split('.')[0] for i in words]

for w in words:
    similarity = [w.path_similarity(j) for j in words]
    similarities.append(similarity)

df = pandas.DataFrame(similarities, columns = words_name, index = words_name)
print(df)

tree2  = swn.senti_synset('tree.n.01')
print(tree2.pos_score())
print(tree2.neg_score())

print (info_word[0].definition())

word = "hate"
info_word = wordnet.synsets(word)
print(info_word)

tree2  = swn.senti_synset('Quit.v.01')
print(tree2.pos_score())
print(tree2.neg_score())

tree3  = swn.senti_synset('Walk.v.01')
print(tree3.pos_score())
print(tree3.neg_score())


wordOne = wordnet.synset("school.n.01")
wordTwo = wordnet.synset("stress.n.01")

print (wordOne.path_similarity(wordTwo))