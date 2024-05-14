#This file is a importable script version of the Jupyter Notebook file.

import pandas as pd
from textblob import TextBlob

def bsa (dataframe, column):
    """This function performs a basic sentiment analysis (polarity, subjectivity) on a given column of a data frame.
    @param datarframe: The data frame to be analyzed.
    @param column: The column of the data frame to be analyzed.
    @return: The data frame with two appended columns, one for the polarity score and one for the subjectivity score."""
    
    for index, row in dataframe.iterrows():
        analysis = TextBlob(str(row[column]))
        dataframe.loc[index, 'polarity'] = analysis.sentiment.polarity
        dataframe.loc[index, 'subjectivity'] = analysis.sentiment.subjectivity
    return dataframe
