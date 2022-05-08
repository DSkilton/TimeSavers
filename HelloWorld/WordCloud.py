

import numpy as np
import matplotlib.pyplot as plt
import PIL.Image
from wordcloud import WordCloud, STOPWORDS

text = open("data.txt", "r").read()
colourmap = ImageColourGenerator(python_mask)

wc= worldcloud(mask=pyton_mask, stopwords=STOPWORDS,
                backround_colour="white", repeat=true
                min_front_size=3).generate("text")
wc.recolour(colour_funk=colourmap)
plt.imshow(wc)
plt.axis("off")
plt. show()