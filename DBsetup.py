import sqlite3

def create_connection():
    connection = sqlite3.connect('concerts.db')
    return connection

def execute_migration(file_path):
    with open(file_path, 'r') as file:
        sql_script = file.read()

    conn = create_connection()
    cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # Run migrations
    execute_migration('migration/band.sql')
    execute_migration('migration/venue.sql')
    execute_migration('migration/concert.sql')
    print("Migrations completed.")