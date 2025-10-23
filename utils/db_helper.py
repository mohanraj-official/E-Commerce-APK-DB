import cx_Oracle
from config import DB_USER, DB_PASS, DB_DSN

def get_connection():
    return cx_Oracle.connect(DB_USER, DB_PASS, DB_DSN)
