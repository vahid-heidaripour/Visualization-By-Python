import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

alice_novel = open('alice.txt', 'r').read()

stopwords = set(STOPWORDS)

alice_mask = np.array(Image.open('alice_mask.png')) # this is a mask

alice_wc = WordCloud(background_color='white',
                     max_words=2000, # first 2000 words
                     mask=alice_mask,  # add this like to show with alice mask
                     stopwords=stopwords)

stopwords.add('said')

alice_wc.generate(alice_novel)


fig = plt.figure()
fig.set_figwidth(14)
fig.set_figheight(18)

plt.imshow(alice_wc, interpolation='bilinear')

plt.axis('off')
plt.show()