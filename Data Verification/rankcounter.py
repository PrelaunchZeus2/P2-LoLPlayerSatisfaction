import pandas as pd
import cassiopeia as cass
import os
import requests
from bs4 import BeautifulSoup
import helpers

MY_API_KEY = os.getenv('RIOT_API_KEY')

#set api key in cassiopeia
cass.set_riot_api_key(MY_API_KEY)

#import data
data = pd.read_csv(r'LolDataCleaned.csv')

for index, row in data.iterrows(): #Iterate through rows to get the players submitted name
    text = row['PlayerStats'] #get submission
    if text == 'Not Provided':
        print('No Submission')
    elif 'https://www.op.gg/' in text: #if submission is an account link to op.gg
        request = requests.get(text) #get the page
        soup = BeautifulSoup(request.content, 'html.parser') 
        rank_ul = soup.find('ul', class_='tier-list')
        if rank_ul is not None: #if there is a list of prev ranks
            rank_text = [li.get_text() for li in rank_ul.findAll('li')] #get the text of each rank
            print(rank_text)
        else:
            print(f"No 'tier-list' ul found in {text}")
    else: #if submission is a summoner name
        acct_info = helpers.get_acct_info_from_text(text)
        print(acct_info)






