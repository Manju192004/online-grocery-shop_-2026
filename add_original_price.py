import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="", # using empty password as in app.py
        database="homedb"
    )
    cursor = conn.cursor()
    cursor.execute("DESCRIBE product")
    columns = [col[0] for col in cursor.fetchall()]
    
    if 'original_price' not in columns:
        cursor.execute("ALTER TABLE product ADD COLUMN original_price DECIMAL(10,2) NULL")
        print("Added 'original_price' column to product table.")
    else:
        print("'original_price' column already exists.")
        
    conn.commit()
    cursor.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")
