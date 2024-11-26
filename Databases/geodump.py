import sqlite3
import json

conn = sqlite3.connect('opengeo.sqlite')
cursor = conn.cursor()

# retrieve the locations from db
cursor.execute("SELECT * FROM Locations")

fh = open("where.js",'w')
fh.write("myData=[\n")
count = 0

for row in cursor:
    data = str(row[1].decode())
    
    try:
        js = json.loads(str(data))
    except:
        continue
    
    if len(js['features']) == 0 : continue

    try:
        lat = js['features'][0]['geometry']['coordinates'][1]
        lng = js['features'][0]['geometry']['coordinates'][0]
        where = js['features'][0]['properties']['display_name']
        where = where.replace("'", "")
        
    except:
        print('Unexpected format')
        # print(js)
    
    try :
        print(where, lat, lng)

        count = count + 1
        if count > 1 : fh.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fh.write(output)
    except:
        continue
fh.write("\n];\n")
cursor.close()
fh.close()
print(count, "records written to where.js")