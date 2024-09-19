CREATE TABLE bands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    hometown TEXT NOT NULL
);
INSERT INTO concerts(id, venue_id, name) VALUES(1, 1, "ian")