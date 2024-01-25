import pandas as pd
import numpy as np 
import re
import data_extraction
df_for_clean = data_extraction.DataExtractor().users
card_df = data_extraction.DataExtractor().card_util
import database_utils
out_db = database_utils.DatabaseConnector().out_engine


class DataCleaning:
    def __init__(self):
       #self.db = self.clean_user_data()
       #self.clean_card = self.clean_card_data()
       pass
    def clean_user_data(self):
     print(df_for_clean)

     regex_expression = '^(?:(?:\(?(?:0(?:0|11)\)?[\s-]?\(?|\+)44\)?[\s-]?(?:\(?0\)?[\s-]?)?)|(?:\(?0))(?:(?:\d{5}\)?[\s-]?\d{4,5})|(?:\d{4}\)?[\s-]?(?:\d{5}|\d{3}[\s-]?\d{3}))|(?:\d{3}\)?[\s-]?\d{3}[\s-]?\d{3,4})|(?:\d{2}\)?[\s-]?\d{4}[\s-]?\d{4}))(?:[\s-]?(?:x|ext\.?|\#)\d{3,4})?$' #Our regular expression to match
     df_for_clean.loc[~df_for_clean['phone_number'].str.match(regex_expression), 'phone_number'] = np.nan

     df_for_clean['phone_number']= df_for_clean['phone_number'].replace('^.*\+44\s*','0', regex=True)
     df_for_clean['phone_number']= df_for_clean['phone_number'].replace('^.*\(\s*','', regex=True)
     df_for_clean['phone_number']= df_for_clean['phone_number'].replace('^.*\)\s*','', regex=True)


     
     df_for_clean.phone_number = df_for_clean.phone_number.replace(np.nan,'0')

     df_for_clean.join_date = df_for_clean.join_date.replace(np.nan,'0')
     df_for_clean.join_date = pd.to_datetime(df_for_clean.join_date, format= 'mixed', errors= 'coerce')
     

     df_for_clean.date_of_birth = df_for_clean.date_of_birth.replace(np.nan,'0')
     df_for_clean.date_of_birth = pd.to_datetime(df_for_clean.date_of_birth, format= 'mixed', errors= 'coerce')

     
     df_for_clean.to_sql('dim_users', out_db, if_exists='replace')

     print(df_for_clean)

    def clean_card_data(): 
     
     
     card_df.reset_index(drop=True,inplace=True)

     card_df['card_number']= card_df['card_number'].replace('^.*\?\s*','', regex=True)
     card_df.date_payment_confirmed = card_df.date_payment_confirmed.replace(np.nan,'0')
     card_df.date_payment_confirmed = pd.to_datetime(card_df.date_payment_confirmed , yearfirst= True, errors= 'coerce')

     card_df.dropna(axis=0, inplace= True)


     card_df.to_sql('dim_card_details',out_db,if_exists= 'replace')
     print(card_df)


 


     
     pass

test = DataCleaning.clean_card_data()