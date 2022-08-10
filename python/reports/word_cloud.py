# Import Matplotlib and WordCloud libraries
import matplotlib.pyplot as plt
from wordcloud import WordCloud

definition = [
             "A tag cloud (also known as a word cloud, wordle or weighted list in visual design)",
             "is a visual representation of text data, which is often used to depict keyword", 
             "metadata on websites, or to visualize free form text. "
            ]

# Join each line of the defitinion list
all_words = ' '.join([text for text in definition])

# Creating the WordCloud with `all_words`
word_cloud_words = WordCloud(width = 800, height = 500, max_font_size = 110,
                          collocations=False).generate(all_words)

# Plotting the image with WordCloud 
plt.figure(figsize = (10,7))
plt.imshow(word_cloud_words, interpolation = 'bilinear')
plt.axis('off')
plt.show()