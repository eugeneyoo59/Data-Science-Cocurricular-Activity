import pandas
import matplotlib.pyplot as plt
import seaborn
from wordcloud import wordcloud, STOPWORDS

data = pandas.read_csv("JoeBidenTweets.csv")
print (data)
print (data.info())
print (data.describe())
print (data.isnull().sum)

data["timestamp"] = pandas.to_datetime(data["timestamp"])
print (data.info())

data = data.drop(columns=['url', 'id'])

data_year = data.groupby(data['timestamp'].dt.year)["likes"].count()
print("---------Biden Tweets per year--------")
print (data_year)
print(data["tweet"])
data_median = data.groupby(data['timestamp'].dt.year)["likes"].median()
print (data_median)

data_mean = data.groupby(data['timestamp'].dt.year)["likes"].mean()
print (data_mean)

data_sum = data.groupby(data['timestamp'].dt.year)["likes"].sum()
print (data_sum)

seaborn.lineplot(x=["timestamp"], y=["likes"], data=data_median)
plt.show()

stopwords = set(STOPWORDS)
print(stopwords)
print(data["tweet"].astype(str))
text=" ".join(t for t in data.tweet)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()