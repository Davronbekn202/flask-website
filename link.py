import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="start",
        user="postgres",
        password="A0B1D9E2",
        host="localhost",
        port=5432
    )

def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS start (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        surname VARCHAR(100),
        age INT )""")

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS passport
                   (id SERIAL PRIMARY KEY,
                    special_id VARCHAR(10),
                    birth_date DATE,
                    user_id INT REFERENCES start(id)
                    )""")
    connection.commit()

create_table()
