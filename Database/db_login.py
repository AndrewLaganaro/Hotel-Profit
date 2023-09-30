from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

class MySQL:
    def __init__(self, database_url: str):
        self.engine = create_engine(database_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.inspector = inspect(self.engine)
        
    def get_conn(self):
        db_session = self.SessionLocal()
        return db_session
    
    def create_tables(self, table_schemas):
        for schema in table_schemas:
            table_name = schema.__tablename__
            
            # Check if the table exists
            table_exists = table_name.lower() in self.inspector.get_table_names().lower()
            
            if not table_exists:
                # The table doesn't exist, so create it
                print(f"Table '{table_name}' doesn't exist. Creating it now...")
                schema.__table__.create(bind=self.engine)
                print(f"Table '{table_name}' created successfully.")
            else:
                print(f"Table '{table_name}' already exists. Skipping creation.")

