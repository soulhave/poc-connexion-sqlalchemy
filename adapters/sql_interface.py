import os

import sqlalchemy

db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
db_name = os.environ.get("DB_NAME")
cloud_sql_instance_name = os.environ.get("CLOUD_SQL_INSTANCE_NAME")


def create_engine():
    return sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername='mysql+pymysql',
            username=db_user,
            password=db_pass,
            database=db_name,
            query={
                'unix_socket': '/cloudsql/{}'.format(cloud_sql_instance_name)
            }
        ),
        pool_size=5,
        max_overflow=2,
        pool_timeout=30,  # 30 seconds
        pool_recycle=1800)
