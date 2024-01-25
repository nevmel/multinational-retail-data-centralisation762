import pandas as pd
from sqlalchemy import create_engine
import psycopg2


class DatabaseConnector:
    """creating a link to the AICore source database 
    Reads from the source YAML file and inserts necessary variable from a dictionary"""

    def __init__(self):
        self.yaml_dict = self.read_db_creds()
        self.engine = self.init_db_engine()
        self.tables = self.list_db_tables()
        self.out_engine = self.upload_to_db()
        pass
    """initailising the 'self' command. Nothing else being passed in at the moment to class"""


            

    def list_db_tables(self):
        
        conn_engine = self.engine.connect() #connect to database from yaml file
        db_tables_df = pd.read_sql('SELECT * FROM information_schema.tables',conn_engine)#what info to collect
        db_tables_list = db_tables_df["table_name"].to_list()#list of all table names in database
        return db_tables_df
        
      
       

    def init_db_engine(self):
        
        """Connect to the AICore RDS Database"""

        # Database connection details
        DATABASE_TYPE = 'postgresql' #type of database being connected to 
        DBAPI = 'psycopg2' #which API is being used to connect (these could be contained in the yaml file, but aren't in this case)
        ENDPOINT = self.yaml_dict["RDS_HOST"] #id details of the store for the database. In this case an AWS cloud location
        USER = self.yaml_dict["RDS_USER"] # Name of user
        PASSWORD = self.yaml_dict["RDS_PASSWORD"] #Password, not transmitted in clear when connecting
        PORT = self.yaml_dict["RDS_PORT"] #standard 5432 in this case, but can be bespoke
        DATABASE = self.yaml_dict["RDS_DATABASE"] # format database is stored in
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}") # Creates the link to use
        return engine

    def read_db_creds(self):
        import yaml
        from pathlib import Path
        yaml_dict = yaml.safe_load(Path("db_creds.yaml").read_text()) #creating dictionary from the YAML file to be passed to init_db_engine
        return yaml_dict
           
    def  upload_to_db(self):   
        #with psycopg2.connect(host='localhost',user='postgres', password= 'Beverly01!', dbname='sales_data',port = 5432) as out_conn:
         
                 # Database connection details
        DATABASE_TYPE = 'postgresql' #type of database being connected to 
        DBAPI = 'psycopg2' #which API is being used to connect (these could be contained in the yaml file, but aren't in this case)
        ENDPOINT = 'localhost' #id details of the store for the database. In this case an AWS cloud location
        USER = 'postgres' # Name of user
        PASSWORD = 'Beverly01!' #Password, not transmitted in clear when connecting
        PORT = '5432' #standard 5432 in this case, but can be bespoke
        DATABASE = 'sales_data' # format database is stored in
        out_conn = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}") # Creates the link to use
         
        return out_conn

        pass        





