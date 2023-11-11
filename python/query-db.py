import psycopg2

def main():
    conn = psycopg2.connect(
            database="rpi",
            host="localhost",
            user="rpi",
            password="alma",
            port="5432",
        )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM leads;")
    print(cursor.fetchall())
