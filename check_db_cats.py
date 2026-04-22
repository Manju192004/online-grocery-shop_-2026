import mysql.connector

def check_cats():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="homedb"
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM category")
        cats = cursor.fetchall()
        for cat in cats:
            print(f"ID: {cat['id']}, Name: {cat['name']}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_cats()
