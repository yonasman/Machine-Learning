import urllib.error, urllib.request,urllib.parse
import sqlite3
import json

# create db connection
conn = sqlite3.connect('./opengeo.sqlite')
cursor = conn.cursor()

# create locations table
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Locations(address TEXT, geodata TEXT)
    '''
)

def read_and_visualize():
    notFound = 0
    count = 0
    # read the where.data file
    fh = open(r"D:\Users\Administrator\Desktop\General\AI-DEVELOPMENT\ML-COURSERA\Machine-Learning\Databases\where.data")

    for line in fh:
        if count > 100:
            print("Retrieved 100 locations, restart to retrieve more")
            break
        address = line
        print('')
        cursor.execute("SELECT geodata FROM Locations WHERE address= ?",
            (address, ))
        try:
            data = cursor.fetchone()[0]
            print("Found in database", address)
            continue
        except:
            pass
        
        try:
            js = json.loads(address)
            # print(js)
        except:
            print(address)
            continue
        
        if not js or 'features' not in js:
            print('==== Download error ===')
            print(data)
            break
        if len(js['features']) == 0:
            print('==== Object not found ====')
            notFound += 1

        cursor.execute('''INSERT INTO Locations (address, geodata)
            VALUES ( ?, ? )''',
            (memoryview(address.encode()), memoryview(data.encode()) ) )

    conn.commit()
read_and_visualize()
        
        

