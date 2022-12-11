import sqlalchemy as db
import os

class Dabatase:
    engine = {}
    connection = {}
    db = {}
    metadata = {}

    def __init__(self):
        try:
            # engine = db.create_engine("postgresql+pg8000://myusername:mypassword@172.17.0.2:5432/postgres")
            print('Connecting to Database')
            engine = db.create_engine(f"postgresql+pg8000://{os.environ['DB_USERNAME']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}")
            connection = engine.connect()
            metadata = db.MetaData
            
            self.db = db
            self.engine = engine
            self.connection = connection
            self.metadata = metadata
            print(f"Database {os.environ['DB_NAME']} Connected")
            return
        except:
            raise
