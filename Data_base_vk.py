import psycopg2
from parol_and_tokens import password


con = psycopg2.connect(
  database="postgres",
  user="postgres",
  password=password,
  host="localhost",
  port="5432")

print("Database opened successfully")

# создание таблицы
# cur = con.cursor()
# cur.execute(
# '''CREATE TABLE Users_search1
# (ID SERIAL PRIMARY KEY NOT NULL,
# First_name TEXT NOT NULL,
# Last_name TEXT NOT NULL,
#              vk_id_user CHAR(50));'''
#         )

# cur.execute(
# '''CREATE TABLE Candidates1
# (ID SERIAL PRIMARY KEY NOT NULL,
# First_name TEXT NOT NULL,
# Last_name TEXT NOT NULL,
# vk_id_user CHAR(50));'''
#  )
# print("Table created successfully")

def insert_bd_candadets(str_response):
    con = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="Parol444!@",
        host="localhost",
        port="5432")
    cur = con.cursor()
    cur.execute(str_response)
    con.commit()

def close_bd():
    con.close()
