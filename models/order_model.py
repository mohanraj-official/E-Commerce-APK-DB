from utils.db_helper import get_connection

def get_all_orders():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT o.ORDER_ID, o.CUSTOMER_ID, c.CUSTOMER_NAME, o.ORDER_DATE, o.TOTAL_AMOUNT
        FROM ORDERS o
        JOIN CUSTOMERS c ON o.CUSTOMER_ID = c.CUSTOMER_ID
    """)
    rows = cur.fetchall()
    cols = [col[0] for col in cur.description]
    conn.close()
    return [dict(zip(cols, row)) for row in rows]

def get_order_items(order_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT oi.ITEM_ID, oi.PRODUCT_ID, p.NAME AS PRODUCT_NAME, oi.QTY, oi.PRICE
        FROM ORDER_ITEMS oi
        JOIN PRODUCTS p ON oi.PRODUCT_ID = p.PRODUCT_ID
        WHERE oi.ORDER_ID = :id
    """, [order_id])
    rows = cur.fetchall()
    cols = [col[0] for col in cur.description]
    conn.close()
    return [dict(zip(cols, row)) for row in rows]
