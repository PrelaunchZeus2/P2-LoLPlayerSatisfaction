#this file is a importable script version of the code in the jupyter notebook
import spacy
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from spacy.lang.en.stop_words import STOP_WORDS
from nltk.probability import FreqDist

def tokwordcloud(dataframe, column, num_words=250, save_as_png=False, filename='wordcloud.png'):
    """This function takes a data frame and a column name as input, then tokenizes the column and creates a word cloud of the tokens.
    @param dataframe: The data frame containing the column
    @param column: The column name to be tokenized and visualized
    @param num_words: The number of most common words to include in the word cloud
    @param save_as_png: Whether or not to save the word cloud as a png file
    @param filename: The name of the file to save the word cloud as"""
    
    nlp = spacy.load('en_core_web_sm') #load english language model
    
    tokens = [] #Holds the tokens
    for response in dataframe[column]: #Create tokens from the responses
        if isinstance(response, str):
            doc = nlp(response)
            tokens.extend([token.lemma_ for token in doc if not token.is_stop and not token.is_punct and not token.is_space])

    freq_dist = FreqDist(tokens) #Identify the frequency of each token
    common_words = freq_dist.most_common(num_words) #Get the num_words most common tokens
    
    wordcloud_string = ' '.join([word for word, _ in common_words])

    wordcloud = WordCloud(width = 2560, height = 1440, 
                background_color ='white', 
                stopwords = STOP_WORDS, 
                min_font_size = 12).generate(wordcloud_string)

    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 

    if save_as_png:
        plt.savefig(filename, format='png')
    else:
        plt.show()
    
    
    
    