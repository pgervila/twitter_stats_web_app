import pandas as pd
from sqlalchemy import create_engine

conn = create_engine("postgresql+psycopg2://postgres:Arnau3.1@localhost/TwitterLangs")

username = "KRLS"

query_1 = """   SELECT username, lang, 100*count(lang)/50. as pct
                FROM tweets t JOIN languages l ON t.lang_id = l.id 
                JOIN users u ON t.user_id = u.id
                WHERE username = '{}'
                GROUP BY username, lang
          """.format(username)

df = pd.read_sql_query(query_1, conn)
