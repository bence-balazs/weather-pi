import psycopg2
from gpiozero import CPUTemperature

def main():
    
    # PG-DB connection detials
    conn = psycopg2.connect(
        database="rpi",
        host="localhost",
        user="rpi",
        password="alma",
        port="5432",
    )

    cpu = CPUTemperature()
    formatted_value = format(cpu.temperature, '.1f')
    cursor = conn.cursor()

    # SQL command to run
    sql ='''INSERT INTO cpu_temp (temp) VALUES (%s)''' % formatted_value
    
    # Execute the insert
    cursor.execute(sql)
    
    # Commit changes to DB
    conn.commit()

    # Close DB connection
    conn.close()

if __name__ == "__main__":
    main()
