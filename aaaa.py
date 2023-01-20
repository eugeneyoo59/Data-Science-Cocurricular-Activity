import pandas
import matplotlib.pyplot as plt
from wordcloud import (WordCloud)
from PIL import Image
import numpy as np
data = pandas.read_csv("game of thrones.csv")
img = Image.open('naver_logo.jpeg')
back_image = np.array(img)


print("TEST")

text = " ".join(title for title in data.Title)

wordcloud1 = WordCloud(mask=back_image, background_color="white", width =1000, height = 1000).generate(text)
plt.imshow(wordcloud1)
plt.axis("off")
plt.show()