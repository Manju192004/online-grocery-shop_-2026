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
        
        # 1. List all tables
        cursor.execute("SHOW TABLES")
        tables = [t[0] for t in cursor.fetchall()]
        print(f"Total tables: {len(tables)}")
        for t in tables:
            print(f"DEBUG: Found table: {t}")
            
        # 2. Check for 'stock_in' specifically
        if 'stock_in' in tables:
            print("\nTable 'stock_in' exists!")
            cursor.execute("SHOW CREATE TABLE stock_in")
            print(cursor.fetchone()[1])
        else:
            print("\nTable 'stock_in' NOT found in SHOW TABLES.")
            
        # 3. Check for any table that might reference 'product'
        print("\nSearching for foreign keys referencing 'product' or 'id'...")
        for t in tables:
            cursor.execute(f"SHOW CREATE TABLE {t}")
            create_stmt = cursor.fetchone()[1]
            if 'REFERENCES `product`' in create_stmt or 'product_id' in create_stmt:
                print(f"\n--- Table {t} ---")
                print(create_stmt)
                
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_tables()
