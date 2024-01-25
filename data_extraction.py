import database_utils #import from a foreign file
from tabula import read_pdf
db_conn = database_utils.DatabaseConnector() #global variable for script, saves a bit of typing every time
import pandas as pd


class DataExtractor:
    """extracting database detail from the link in database_utils"""
    def __init__():

       pass

    def read_rds_table():
       
        read_rds_table_df = pd.read_sql_query('SELECT * FROM legacy_users',db_conn.engine)
        

        return read_rds_table_df
    
    def retrieve_pdf_data():
        """Process to retrieve data stored in a PDF
        TABULA add on for Pyton (see top of file)
        IMPORT the read-pdf function
        
        """

        pdf_link = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf'#held as a variable so that can be changed easily at a later date.
        card_data = read_pdf(pdf_link, pages= 'all') #pages= 'all' or only the first page is imported to dataframe
        card_data_df = pd.concat(card_data)   #each page of PDF is a seperate list, so needs to be concatenated

        return card_data_df



        

        pass



