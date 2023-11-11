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

    # Set database timezone to CET
    cursor.execute("SET timezone = 'CET';")
    # Drop the table if already exists
    cursor.execute("DROP TABLE IF EXISTS cpu_temp")

    # Table create command
    sql ='''CREATE TABLE cpu_temp(
        id SERIAL PRIMARY KEY,
        time TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
        temp REAL
        )
        '''

    # Create the table and commit
    cursor.execute(sql)
    conn.commit()
    
    # Closing the connection
    conn.close()

if __name__ == "__main__":
    main()
