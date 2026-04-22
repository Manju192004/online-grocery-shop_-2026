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
            print(f"- {t}")
            
        # 2. Check each table for references to 'product' or 'id'
        print("\nAnalyzing table structures for references...")
        for t in tables:
            try:
                cursor.execute(f"SHOW CREATE TABLE `{t}`")
                create_stmt = cursor.fetchone()[1]
                if 'product_id' in create_stmt.lower() or 'REFERENCES `product`' in create_stmt:
                    print(f"\n--- Table: {t} ---")
                    print(create_stmt)
            except Exception as e:
                print(f"Error reading table {t}: {e}")
                
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_tables()
