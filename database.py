import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="student_portal",
            user="postgres",
            password="nikita09",
            port="5433"
        )
        return connection

    except Exception as e:
        print("Database Connection Error:", e)
        return None


def create_table():
    connection = get_connection()

    if connection:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                course VARCHAR(100) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        connection.commit()
        cursor.close()
        connection.close()
        print("Student table created successfully!")