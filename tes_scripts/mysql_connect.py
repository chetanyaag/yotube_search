import mysql.connector

try:
    connection = mysql.connector.connect(
        host='127.0.0.1', 
        user='chetanya',
        password='password',
        port=3306
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
        title TEXT,
        youtube_video_id VARCHAR(255) UNIQUE,
        youtube_raw_response TEXT,
        duration INT,
        is_uploaded_s3 BOOL DEFAULT 0,
        is_deleted_server BOOL DEFAULT 0,
        s3_link VARCHAR(255),
        s3_filename VARCHAR(255),
        is_uploaded_instagram BOOL DEFAULT 0,
        is_deleted_s3 BOOL DEFAULT 0, 
        instagram_container_id VARCHAR(255),
        instagram_published_id VARCHAR(255)
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
