DROP TABLE IF EXISTS concerts;
CREATE TABLE concerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    band_id INTEGER,
    venue_id INTEGER,
    date TEXT NOT NULL,
    FOREIGN KEY (band_id) REFERENCES bands(id),
    FOREIGN KEY (venue_id) REFERENCES venues(id)
);