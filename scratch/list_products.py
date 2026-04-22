import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root", 
        database="homedb"
    )
    cursor = conn.cursor()
    cursor.execute('SELECT product_name FROM product')
    products = cursor.fetchall()
    with open('products_list.txt', 'w', encoding='utf-8') as f:
        for p in products:
            f.write(p[0] + '\n')
    print("Product list saved to products_list.txt")
except Exception as e:
    print(f"Error: {e}")
finally:
    if 'cursor' in locals(): cursor.close()
    if 'conn' in locals(): conn.close()
