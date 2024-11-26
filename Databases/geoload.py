import http
import urllib.error, urllib.request,urllib.parse
import sqlite3
import json
import ssl
import time
import sys

# service base url
serviceUrl = 'https://py4e-data.dr-chuck.net/opengeo?'

# create db connection
conn = sqlite3.connect('./opengeo.sqlite')
cursor = conn.cursor()

# create locations table
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Locations(address TEXT, geodata TEXT)
    '''
)
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def read_and_visualize():
    notFound = 0
    count = 0
    # read the where.data file
    fh = open(r"D:\Users\Administrator\Desktop\General\AI-DEVELOPMENT\ML-COURSERA\Machine-Learning\Databases\where.data")

    for line in fh:
        if count > 100:
            print("Retrieved 100 locations, restart to retrieve more")
            break
        address = line.strip()
        print('')
        cursor.execute("SELECT geodata FROM Locations WHERE address= ?",
            (memoryview(address.encode()), ))
        try:
            data = cursor.fetchone()[0]
            print("Found in database", address)
            continue
        except:
            pass
        # extract the query param and build the complete url
        params = dict()
        params['q'] = address

        url = serviceUrl + urllib.parse.urlencode(params)
        
        # retrieve data from the url
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        print("Retrieved", len(data), data[:20].replace('\n',''))
        count += 1
        
        try:
            js = json.loads(data)
            # print(js)
        except:
            print(data)
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
        
        

