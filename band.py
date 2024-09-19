import sqlite3

class Band:
    def __init__(self, band_id):
        self.band_id = band_id
    
    def concerts(self):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM concerts WHERE band_id = ?", (self.band_id,))
        results = cursor.fetchall()
        conn.close()
        return results

    def venues(self):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT venues.* 
            FROM venues 
            JOIN concerts ON venues.id = concerts.venue_id 
            WHERE concerts.band_id = ?;
        """, (self.band_id,))
        results = cursor.fetchall()
        conn.close()
        return results