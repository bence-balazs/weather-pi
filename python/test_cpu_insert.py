import psycopg2
import datetime
from datetime import timezone

def main():
    conn = psycopg2.connect(
            database="rpi",
            host="localhost",
            user="rpi",
            password="alma",
            port="5432",
        )

    cursor = conn.cursor()

    # Table create command
    sql ='''INSERT INTO cpu_temp (temp)
            VALUES (33.9)
        '''

    # Load test data
    cursor.execute(sql)
    conn.commit()
    
    # Closing the connection
    conn.close()

if __name__ == "__main__":
    main()
