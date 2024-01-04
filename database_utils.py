class DatabaseConnector:
    """creating a link to the AICore source database 
    Reads from the source YAML file and inserts necessary variable from a dictionary"""

    def __init__(self):
        pass
    """initailising the 'self' command. Nothing else being passed in at the moment to class"""

 
       

    def init_db_engine(self,yaml_dict):
        """Connect to the AICore RDS Database"""
        import psycopg2
        conn = psycopg2.connect(
        host=yaml_dict["RDS_HOST"], #reading the dictionary for each of the values
        port=yaml_dict["RDS_PORT"],
        database=yaml_dict["RDS_DATABASE"],
        user=yaml_dict["RDS_USER"],
        password=yaml_dict["RDS_PASSWORD"])
        conn.close() #closing the open connection
        

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