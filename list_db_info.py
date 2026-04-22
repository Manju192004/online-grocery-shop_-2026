import mysql.connector

def list_tables():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="homedb"
        )
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print("Tables in homedb:")
        for table in tables:
            print(f"- {table[0]}")
            
        # Also show foreign keys for important tables
        for table in ['stock_in', 'feedback', 'orders']:
            try:
                cursor.execute(f"SHOW CREATE TABLE {table}")
                print(f"\nStructure for {table}:")
                print(cursor.fetchone()[1])
            except:
                print(f"\nTable {table} not found or error.")
                
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_tables()
