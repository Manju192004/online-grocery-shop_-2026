import mysql.connector
from datetime import datetime

def verify_logic():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="homedb"
        )
        cursor = conn.cursor(dictionary=True, buffered=True)
        
        # 1. Get a product
        cursor.execute("SELECT id, quantity FROM product LIMIT 1")
        product = cursor.fetchone()
        if not product:
            print("No products found to test.")
            return
        
        pid = product['id']
        old_qty = product['quantity']
        test_qty = 50
        
        print(f"Testing with Product ID {pid}. Current Qty: {old_qty}")
        
        # 2. Simulate save_stockin logic
        try:
            # Insert into stock_in
            cursor.execute("""
                INSERT INTO stock_in (product_id, supplier_name, supplier_address, quantity, price, total_amount, date_added) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (pid, 'Test Supplier', '123 Test St', test_qty, 10.0, 500.0, datetime.now()))
            
            # Update product
            cursor.execute("UPDATE product SET quantity = quantity + %s WHERE id = %s", (test_qty, pid))
            
            conn.commit()
            print(f"Committed update. Added {test_qty} units.")
            
            # 3. Verify
            cursor.execute("SELECT quantity FROM product WHERE id = %s", (pid,))
            new_qty = cursor.fetchone()['quantity']
            print(f"New Qty: {new_qty}")
            
            if new_qty == old_qty + test_qty:
                print("SUCCESS: Quantity updated correctly in product table.")
            else:
                print(f"FAILURE: Expected {old_qty + test_qty}, got {new_qty}")
            
            # 4. Check history
            cursor.execute("SELECT * FROM stock_in ORDER BY id DESC LIMIT 1")
            last_entry = cursor.fetchone()
            print(f"Last stock_in entry: {last_entry['supplier_name']} - {last_entry['quantity']} units")

            # Cleanup
            cursor.execute("UPDATE product SET quantity = %s WHERE id = %s", (old_qty, pid))
            cursor.execute("DELETE FROM stock_in WHERE id = %s", (last_entry['id'],))
            conn.commit()
            print("Cleanup complete.")

        except Exception as e:
            conn.rollback()
            print(f"Error during logic test: {e}")
            
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    verify_logic()
