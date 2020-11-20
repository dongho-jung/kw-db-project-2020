import itertools

import sqlalchemy
import psycopg2

def execute(cmd):
    with psycopg2.connect(user='postgres', database='kw_db') as conn:
        with conn.cursor() as cur:
            cur.execute(cmd)

def fetch(cmd):
    with psycopg2.connect(user='postgres', database='kw_db') as conn:
        with conn.cursor() as cur:
            cur.execute(cmd)
            result = cur.fetchall()
            if len(result[0]) == 1:
                return list(itertools.chain.from_iterable(result))
            else:
                return result

def insert(df, table_name):
    engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres@/kw_db')
    with engine.begin() as conn:
        df.to_sql(table_name, conn, if_exists='append', method='multi', chunksize=5000, index=False)
