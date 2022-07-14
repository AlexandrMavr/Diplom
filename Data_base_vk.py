import psycopg2
from config import database, user, password, host, port

class CandidatInBase():
    """для внесения в базу данных"""
    def __init__(self, database, user, password, host, port, str_response):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.str_response = str_response

    @staticmethod
    def insert_bd_candadets(str_response):
        con = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port)
        cur = con.cursor()
        cur.execute(str_response)
        con.commit()

    @staticmethod
    def close_bd():
        con = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port)
        con.close()
