import mysql.connector

try:
    connection = mysql.connector.connect(
        host='127.0.0.1', 
        user='test',
        password='test',
        port=3307
    )

    if connection.is_connected():
        print("Connected to MySQL database")

    cursor = connection.cursor()


    new_database = "botverse"
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {new_database}")
    cursor.execute(f"USE {new_database}")
    create_table_query = """
    CREATE TABLE IF NOT EXISTS videos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT
    )
    """
    cursor.execute(create_table_query)
    print(f"Table videos created successfully")


except mysql.connector.Error as err:
    print("Error:", err)

finally:
    # Close the cursor and connection when done
    if 'connection' in locals():
        cursor.close()
        connection.close()
        print("MySQL connection closed")
