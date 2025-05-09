import os

os.environ["DATABASE_URL"] = "mysql://root:@localhost:888/testdb"

from dj_database_url import config
print(config())


from dj_database_url import parse as db_url_parse
print(db_url_parse("sqlite://:memory:"))


