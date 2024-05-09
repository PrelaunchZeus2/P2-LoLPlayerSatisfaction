import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import pipeline

def Column_Summarizer(dataframe, column):
    """This function takes a data frame and a specified column then generates a summary and keywords for each response in the column, then returns a dataframe with the original column and two new columns appended, one for keywords and one for summaries
    @param dataframe: a pandas dataframe
    @param columnL a string representing the column name
    @return dataframe: the param dataframe with two new columns appended, one for keywords and one for summaries"""
    #something something summerization pipeline
    summarizer = pipeline("summarization")

    #Load Responses
    column_responses = dataframe[column]

    #use the thingy(TF-IDF) to extract key words
    vectorizer = TfidfVectorizer(stop_words='english')
    output_matrix = vectorizer.fit_transform(column_responses)
    keyword = vectorizer.get_feature_names_out()

    #use the summarization pipeline!
    summaries = []
    for response in column_responses:
        summary = summarizer(column_responses, max_length = 20, min_length = 5, do_sample = False)[0]
        print(summary['summary_text'])
        summaries.append(summary['summary_text'])

    #append our results to the data frame
    dataframe[column + '_Keywords'] = [keyword for _ in column_responses]
    dataframe[column + '_Summaries'] = summaries

    return dataframe

#Load data from csv to pd dataframe
LolData = pd.read_csv('Start Here!\LolDataCleaned.csv')

Lol_Data_With_Summaries = Column_Summarizer(LolData, 'OpenChanges')
print(Lol_Data_With_Summaries)