from sqlalchemy.orm import sessionmaker

from adapters.sql_interface import create_engine


class BaseDao:
    session = None

    def __init__(self):
        self.session = sessionmaker(bind=create_engine())()
