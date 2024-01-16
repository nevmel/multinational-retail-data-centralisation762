import database_utils #import from a foreign file
db_conn = database_utils.DatabaseConnector() #global variable for script, saves a bit of typing every time
import pandas as pd


class DataExtractor:
    """extracting database detail from the link in database_utils"""
    def __init__(self):
       self.users = self.read_rds_table()
       pass

    def read_rds_table(self):
       
        read_rds_table_df = pd.read_sql_query('SELECT * FROM legacy_users',db_conn.engine)

        return read_rds_table_df
        pass


