# Variables: Int, float, bool, str.

abc = "THIS is my my string"
print(abc)
abc = abc.lower()
print (abc)
word_list = []
word_list=abc.split()
print(word_list)
print(len(word_list))

#dictionary vs. List ==> {} vs [], key-value vs. value
dic = {}
cnt=0

#for i in word_list:
  #  dic[cnt] = i
 #   cnt = cnt+1

for i in word_list:
    count = dic.get(i, 0)
    if count == 0:
        dic[i] = 1
    else: dic[i] = dic[i]+1
print(dic)