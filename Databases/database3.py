import sqlite3

# Create SQLite connection
conn = sqlite3.connect('tracksDB.sqlite')
cursor = conn.cursor()

# Function to read the CSV and populate the database
def csv_reader():
    # Drop existing tables to ensure a clean slate
    cursor.execute('DROP TABLE IF EXISTS Artist')
    cursor.execute('DROP TABLE IF EXISTS Genre')
    cursor.execute('DROP TABLE IF EXISTS Album')
    cursor.execute('DROP TABLE IF EXISTS Track')

    # Create tables
    cursor.execute('''
        CREATE TABLE Artist (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE
        )
    ''')
    cursor.execute('''
        CREATE TABLE Genre (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE
        )
    ''')
    cursor.execute('''
        CREATE TABLE Album (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            artist_id INTEGER,
            title TEXT UNIQUE
        )
    ''')
    cursor.execute('''
        CREATE TABLE Track (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            title TEXT UNIQUE,
            album_id INTEGER,
            genre_id INTEGER,
            len INTEGER, rating INTEGER, count INTEGER
        )
    ''')

    # Read the CSV file
    with open('tracks.csv') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if len(line) < 7:
                continue
            
            # Extract columns from CSV
            pieces = line.split(',')
            title, artist, album, count, rating, length, genre = pieces[:7]

            # Insert or ignore Artist
            cursor.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
            cursor.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
            artist_id = cursor.fetchone()[0]
            
            # Insert or ignore Album
            cursor.execute('INSERT OR IGNORE INTO Album (artist_id, title) VALUES (?, ?)', (artist_id, album))
            cursor.execute('SELECT id FROM Album WHERE title = ?', (album,))
            album_id = cursor.fetchone()[0]

            # Insert or ignore Genre
            cursor.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
            cursor.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
            genre_id = cursor.fetchone()[0]

            # Insert Track
            cursor.execute('''
                INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) 
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (title, album_id, genre_id, int(length), int(rating), int(count)))

    # Commit changes
    conn.commit()

    # Query the database to verify
    cursor.execute('''
    SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track 
    JOIN Album ON Track.album_id = Album.id
    JOIN Artist ON Album.artist_id = Artist.id
    JOIN Genre ON Track.genre_id = Genre.id
    ORDER BY Artist.name, Track.title 
    LIMIT 3
''')

# Call the CSV reader function
csv_reader()
