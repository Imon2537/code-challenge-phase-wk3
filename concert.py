import sqlite3

class Concert:
    def __init__(self, concert_id):
        self.concert_id = concert_id
    
    @staticmethod
    def find(concert_id):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM concerts WHERE id = ?", (concert_id,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return Concert(result[0])
        return None

    def band(self):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bands WHERE id = (SELECT band_id FROM concerts WHERE id = ?)", (self.concert_id,))
        result = cursor.fetchone()
        conn.close()
        return result

    def venue(self):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM venues WHERE id = (SELECT venue_id FROM concerts WHERE id = ?)", (self.concert_id,))
        result = cursor.fetchone()
        conn.close()
        return result