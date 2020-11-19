import sqlite3

DB_NAME = "mes.db"

def setup():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        # Create table
        c.execute('''CREATE TABLE measurements
                     (measurements integer, created_at real)''')
        conn.commit()

def insert(num: int, timestamp: float):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        inputs = (num, timestamp)
        c.execute("""
           INSERT INTO measurements VALUES (?, ?) 
        """, inputs)
        conn.commit()

def get_all():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("SELECT * from measurements")
        return c.fetchall()

if __name__ == "__main__":
    setup()
