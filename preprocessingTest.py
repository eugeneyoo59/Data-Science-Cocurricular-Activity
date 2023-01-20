from nltk.tokenize import WordPunctTokenizer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import stopwords
text= "These are my sample texts"
print(text)
result = WordPunctTokenizer().tokenize(text)
print (result)
lemmatizer = WordNetLemmatizer()
result2 = lemmatizer.lemmatize("drinks")

print(result2)
list_postLem = []
cnt = 0
for word in result:
    lemm = lemmatizer.lemmatize(word)
    list_postLem.append(lemm)

for word in result:
    if word in stopwords.words("english"):
        result.remove(word)

print(list_postLem)
print(pos_tag(list_postLem))
print(stopwords.words('english'))
print (result)