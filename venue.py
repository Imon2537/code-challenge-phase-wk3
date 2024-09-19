import sqlite3

class Venue:
    def __init__(self, venue_id):
        self.venue_id = venue_id
    
    def concerts(self):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM concerts WHERE venue_id = ?", (self.venue_id,))
        results = cursor.fetchall()
        conn.close()
        return results

    def bands(self):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT bands.* 
            FROM bands 
            JOIN concerts ON bands.id = concerts.band_id 
            WHERE concerts.venue_id = ?;
        """, (self.venue_id,))
        results = cursor.fetchall()
        conn.close()
        return results