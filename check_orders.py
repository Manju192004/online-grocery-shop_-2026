import mysql.connector

def check_orders_table():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="homedb"
        )
        cursor = conn.cursor()
        cursor.execute("DESCRIBE orders")
        columns = [col[0] for col in cursor.fetchall()]
        print(f"Orders columns: {columns}")
        if 'status' not in columns:
            cursor.execute("ALTER TABLE orders ADD COLUMN status VARCHAR(20) DEFAULT 'Pending'")
            print("Added 'status' column to orders table.")
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_orders_table()
