# import psycopg2
#
# con = psycopg2.connect(
#   database="Database",
#   user="postgres",
#   password="R29062011Z",
#   host="127.0.0.1",
#   port="5433"
# )
#
# print("Database opened successfully")
from contextlib import closing
import psycopg2

db = psycopg2.connect("host=localhost dbname=postgres user=postgres password=R29062011Z port=5433")

print("Database opened successfully")
