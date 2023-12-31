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

    cursor.execute("SELECT time at time zone 'Europe/Budapest', temp FROM cpu_temp;")
    print(cursor.fetchall())


if __name__ == "__main__":
    main()
