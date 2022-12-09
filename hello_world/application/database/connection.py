import sqlalchemy as db

class Dabatase:
    engine = {}
    connection = {}
    db = {}
    metadata = {}

    def __init__(self):
        try:
            engine = db.create_engine("postgresql+psycopg2://myusername:mypassword@172.17.0.2:5432/postgres")
            connection = engine.connect()
            metadata = db.MetaData
            
            self.db = db
            self.engine = engine
            self.connection = connection
            self.metadata = metadata
            return
        except:
            raise
