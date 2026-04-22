import mysql.connector

def setup_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="homedb"
        )
        cursor = conn.cursor()
        
        # Create category table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS category (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                description TEXT,
                image VARCHAR(255)
            )
        """)
        
        # Check if feedback table needs modification (e.g., adding rating)
        cursor.execute("DESCRIBE feedback")
        columns = [col[0] for col in cursor.fetchall()]
        if 'rating' not in columns:
            cursor.execute("ALTER TABLE feedback ADD COLUMN rating INT DEFAULT 5")
            print("Added 'rating' column to feedback table.")
            
        conn.commit()
        print("Database setup complete.")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    setup_db()
