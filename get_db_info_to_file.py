import mysql.connector

def get_stock_in_info():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="homedb"
        )
        cursor = conn.cursor()
        
        with open("db_structure_output.txt", "w") as f:
            # List all tables first
            cursor.execute("SHOW TABLES")
            tables = [t[0] for t in cursor.fetchall()]
            f.write(f"Tables: {', '.join(tables)}\n\n")
            
            for t in tables:
                try:
                    cursor.execute(f"SHOW CREATE TABLE `{t}`")
                    f.write(f"--- Table: {t} ---\n")
                    f.write(cursor.fetchone()[1])
                    f.write("\n\n")
                except Exception as e:
                    f.write(f"Error reading table {t}: {e}\n\n")
                    
        cursor.close()
        conn.close()
        print("Done. Check db_structure_output.txt")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_stock_in_info()
