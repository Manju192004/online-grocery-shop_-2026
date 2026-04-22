import mysql.connector

def remove_products():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root", 
            database="homedb"
        )
        cursor = conn.cursor()
        
        # Product names to remove
        products_to_remove = ['chilli', 'birinjal', 'potato']
        
        print("Searching for products...")
        for name in products_to_remove:
            # Using LIKE to catch variations if any
            query = "DELETE FROM product WHERE product_name LIKE %s"
            cursor.execute(query, (f"%{name}%",))
            print(f"Removed items matching '{name}': {cursor.rowcount} rows affected.")
        
        conn.commit()
        print("Success: Products removed from database.")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

if __name__ == "__main__":
    remove_products()
