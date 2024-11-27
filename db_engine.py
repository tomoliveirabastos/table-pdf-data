from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import environ
def get_session(engine):
    s = sessionmaker(bind=engine)
    session = s()
    return session

def get_engine_session():
    connection_string = "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(
        environ['DB_USERNAME'], 
        environ['DB_PASSWORD'],
        environ['DB_HOST'],
        environ['DB_PORT'],
        environ['DB_DATABASE'])

    engine = create_engine(connection_string, echo=False)
    session = get_session(engine)

    return engine, session