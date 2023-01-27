from wordcloud import WordCloud
import matplotlib.pyplot as plt

# open the text file
with open("cloudtext.txt", "r") as f:
    text = f.read()

# generate the word cloud
wordcloud = WordCloud().generate(text)

# display the word cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()