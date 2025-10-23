from utils.db_helper import get_connection

def get_all_customers():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM CUSTOMERS")
    rows = cur.fetchall()
    cols = [col[0] for col in cur.description]
    conn.close()
    return [dict(zip(cols, row)) for row in rows]
