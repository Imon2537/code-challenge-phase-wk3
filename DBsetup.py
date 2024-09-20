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

def insert_band(name, hometown):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bands (name, hometown) VALUES (?, ?)", (name, hometown))
    conn.commit()
    conn.close()

def insert_venue(title, city):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO venues (title, city) VALUES (?, ?)", (title, city))
    conn.commit()
    conn.close()

def insert_concert(band_id, venue_id, date):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)", (band_id, venue_id, date))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # Run migrations
    execute_migration('migration/band.sql')
    execute_migration('migration/venue.sql')
    execute_migration('migration/concert.sql')
    
    # Insert sample data
    insert_band("Sautisol", "Kenya")
    insert_band("Watendawili", "Kenya")
    
    insert_venue("Quivers", "kitengela")
    insert_venue("village market", "runda")
    
    insert_concert(1, 1, "2024-09-20")
    insert_concert(2, 2, "2024-10-05")
    
    print("Migrations completed and data inserted.")
