from flask import g
import sqlite3

def conn_db():
    sql = sqlite3.connect(r'C:\Users\Khoshkar\PycharmProjects\Member_API\application\database\database.db')
    sql.row_factory = sqlite3.Row
    return sql
def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = conn_db()
        return g.sqlite_db