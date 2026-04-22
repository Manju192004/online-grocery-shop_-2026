import mysql.connector

def update_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="homedb"
        )
        cursor = conn.cursor()
        
        # Add date_added to stock_in if it doesn't exist
        try:
            cursor.execute("DESCRIBE stock_in")
            columns = [col[0] for col in cursor.fetchall()]
            if 'date_added' not in columns:
                cursor.execute("ALTER TABLE stock_in ADD COLUMN date_added DATETIME")
                print("Added 'date_added' column to stock_in table.")
            else:
                print("'date_added' column already exists in stock_in table.")
        except Exception as e:
            print(f"Error checking stock_in table: {e}")
            # If table doesn't exist, create it (matching my insertions)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS stock_in (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    product_id INT,
                    supplier_name VARCHAR(255),
                    supplier_address TEXT,
                    quantity INT,
                    price DECIMAL(10,2),
                    total_amount DECIMAL(10,2),
                    date_added DATETIME
                )
            """)
            print("Created stock_in table.")

        conn.commit()
        print("Database update complete.")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_db()
