import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="", 
        database="homedb"
    )
    cursor = conn.cursor()
    cursor.execute("DESCRIBE product")
    columns = [col[0] for col in cursor.fetchall()]
    
    if 'unit' not in columns:
        cursor.execute("ALTER TABLE product ADD COLUMN unit VARCHAR(50) DEFAULT '1 Kg'")
        print("Added 'unit' column.")
    
    if 'description' not in columns:
        cursor.execute("ALTER TABLE product ADD COLUMN description TEXT")
        print("Added 'description' column.")
        
    conn.commit()
    cursor.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")
