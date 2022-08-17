import nltk
import matplotlib as plt
import pandas as pd
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS

df = pd.read_csv("emotions.txt")
df = df[df['Score'] != 3]
df['sentiment'] = df['Score'].apply(lambda rating : +1 if rating > 3 else -1)

text = open("data.txt", "r").read()
stopwords = set(STOPWORDS)
stopwords.update(["br", "href"])
textt = " ".join(review for review in df.Text)
wordcloud = WordCloud(stopwords=stopwords).generate(textt)


plt.imshow(wordcloud)
plt.axis("off")
plt.show()