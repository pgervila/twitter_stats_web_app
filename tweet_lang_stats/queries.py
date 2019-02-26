import pandas as pd

username="KRLS"

query_1 = """   SELECT username, lang, 100*count(lang)/50. as pct
                FROM TWEETS t join languages l ON t.lang_id = l.id 
                JOIN users u ON t.user_id = u.id
                WHERE username = {}
                GROUP BY username, lang
          """.format(username)