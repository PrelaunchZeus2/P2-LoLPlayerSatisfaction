object (account_info):
    def __init__(self, region, acct_name, acct_tag):
        self.region = region
        self.name = acct_name
        self.tag = acct_tag
    
    def __str__(self):
        return f"Region: {self.region}, Acct Name: {self.name}, Acct Tag: {self.tag}"


    def get_acct_info_from_text(text):

        acct_name = text.split('#')[0] #get the account name
        acct_tag = "#"
        if '#' in text:
            acct_tag += (text.split('#')[1]).upper()
        else:
            acct_tag = None
        region = check_region(text)
        

    def check_region(input):
        '''This function reads through the submitted text to check if it has a region code attached in it. If it does, it returns the region code. If it doesn't, it returns None.'''
        regions = ['br', 'eune', 'euw', 'jp', 'kr', 'lan', 'las', 'na', 'oce', 'tr', 'ru']
        for region in regions:
            if region in input.lower():
                return region.upper()
            else:
                return None
