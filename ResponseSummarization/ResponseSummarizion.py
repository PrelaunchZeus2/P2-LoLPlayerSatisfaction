#This script is used to summarize responses from a specified column in a data frame and extract keywords from the responses
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import pipeline

def Column_Summarizer(dataframe, column):
    """This function takes a data frame and a specified column then generates a summary and keywords for each response in the column, then returns a dataframe with the original column and two new columns appended, one for keywords and one for summaries
    @param dataframe: a pandas dataframe
    @param columnL a string representing the column name
    @return dataframe: the param dataframe with two new columns appended, one for keywords and one for summaries"""
    #something something summarization pipeline
    summarizer = pipeline("summarization")

    #Load Responses
    column_responses = dataframe[column].fillna('')  # Fill NaN values with an empty string

    #use the thingy(TF-IDF) to extract key words
    vectorizer = TfidfVectorizer(stop_words='english')
    output_matrix = vectorizer.fit_transform(column_responses)
    keyword = vectorizer.get_feature_names_out()

    #use the summarization pipeline!
    summaries = []
    for response in column_responses:
        if response:  # Only summarize if the response is not an empty string
            summary = summarizer(response, max_length = 20, min_length = 5, do_sample = False)[0]
            summaries.append(summary['summary_text'])
        else:
            summaries.append('')  # If the response is an empty string, append an empty string to the summaries

    #append our results to the data frame
    dataframe[column + '_Keywords'] = [keyword for _ in column_responses]
    dataframe[column + '_Summaries'] = summaries

    return dataframe

    #append our results to the data frame
    dataframe[column + '_Keywords'] = [keyword for _ in column_responses]
    dataframe[column + '_Summaries'] = summaries

    return dataframe