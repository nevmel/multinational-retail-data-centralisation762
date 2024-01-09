class DatabaseConnector:
    """creating a link to the AICore source database 
    Reads from the source YAML file and inserts necessary variable from a dictionary"""

    def __init__(self):
        pass
    """initailising the 'self' command. Nothing else being passed in at the moment to class"""

 
       
        

    def init_db_engine(self,yaml_dict):
        
        """Connect to the AICore RDS Database"""

        from sqlalchemy import create_engine

        # Database connection details
        DATABASE_TYPE = 'postgresql' #type of database being connected to 
        DBAPI = 'psycopg2' #which API is being used to connect (these could be contained in the yaml file, but aren't in this case)
        ENDPOINT = yaml_dict["RDS_HOST"] #id details of the store for the database. In this case an AWS cloud location
        USER = yaml_dict["RDS_USER"] # Name of user
        PASSWORD = yaml_dict["RDS_PASSWORD"] #Password, not transmitted in clear when connecting
        PORT = yaml_dict["RDS_PORT"] #standard 5432 in this case, but can be bespoke
        DATABASE = yaml_dict["RDS_DATABASE"] # format database is stored in
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}") # Creates the link to use
        print(engine) #just a working check line
        
        

        

    def list_db_tables(self,engine,yaml_dict):
        import pandas as pd
        conn_engine = engine.connect()

        db_tables = pd.read_sql('SELECT table_name FROM information_schema.tabls WHERE table_schema =' + yaml_dict["RDS_DATABASE"],conn_engine)

        db_tables_list = db_tables["TABLE_NAME"].to_list()
        print(db_tables_list)
        
    

  


    def read_db_creds(self):
        import yaml
        from pathlib import Path
        yaml_dict = yaml.safe_load(Path("db_creds.yaml").read_text()) #creating dictionary from the YAML file to be passed to init_db_engine
        print(yaml_dict) #just to check something is happening
        self.init_db_engine(yaml_dict)#pass the dict to the next method
        
        






def testing(): #just here to test the above class coding
    test = DatabaseConnector()
    test.read_db_creds()
   
    

testing()