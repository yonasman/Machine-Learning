import sqlite3
import urllib.request
import ssl

def counting_email():
    # Create or connect to a SQLite database
    conn = sqlite3.connect('emailCountDB.sqlite')
    cursor = conn.cursor()

    # Drop the table if it exists
    cursor.execute('DROP TABLE IF EXISTS counts')
    cursor.execute('CREATE TABLE counts(org TEXT, count INTEGER)')

    # Prompt for URL input
    url = input("Enter file URL: ")
    # Set up SSL context to ignore SSL certificate errors
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    # Provide a default URL if none is entered
    if len(url) < 1:
        url = 'https://www.py4e.com/code3/mbox.txt?PHPSESSID=f4ee60bc82018a74c5c08136b0030844'

    try:
        # Make a request to the URL and read the file
        response = urllib.request.urlopen(url, context=ssl_context)
        data = response.read().decode()

        # Process the data
        for line in data.splitlines():
            if line.startswith('From:'):
                # Extract the organization (domain) part of the email address
                domain = line.split('@')[-1]
                cursor.execute(
                    'SELECT count FROM counts WHERE org = ?',
                    (domain,)
                )
                row = cursor.fetchone()
                if row is None:
                    # Insert the domain if it's not already in the database
                    cursor.execute(
                        'INSERT INTO counts (org, count) VALUES (?, 1)',
                        (domain,)
                    )
                else:
                    # Update the count for the domain
                    cursor.execute(
                        'UPDATE counts SET count = count + 1 WHERE org = ?',
                        (domain,)
                    )
        conn.commit()

        # Display the contents of the database
        print("Counts:")
        for row in cursor.execute('SELECT org, count FROM counts ORDER BY count DESC'):
            print(row)

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        conn.close()

# counting_email()
import sqlite3

def email_count3():
    # Dictionary to store domain count
    count_map = dict()

    # Prompt user to enter the file name
    fname = input("Enter the file name: ")

    try:
        # Open the file and process lines
        with open(fname, 'r') as file:
            lines = file.readlines()

            for line in lines:
                if line.startswith("From:"):
                    email = line.split()[1]
                    domain = email.split('@')[-1]
                    
                    # Count the domain occurrences
                    if domain in count_map:
                        count_map[domain] += 1
                    else:
                        count_map[domain] = 1
        
        # Print domain counts
        print("Domain Counts:")
        for domain, count in count_map.items():
            print(f'{domain} --- {count}')

        # Create SQLite connection and insert data into the database
        conn = sqlite3.connect('emailCountDB.sqlite')
        cursor = conn.cursor()

        # Drop the table if it exists and create it
        cursor.execute('DROP TABLE IF EXISTS counts')
        cursor.execute('CREATE TABLE counts (org TEXT, count INTEGER)')

        # Insert domain counts into the table
        for domain, count in count_map.items():
            cursor.execute('INSERT INTO counts (org, count) VALUES (?, ?)', (domain, count))

        # Commit changes
        conn.commit()

        # Display the counts sorted by descending order
        cursor.execute('SELECT * FROM counts ORDER BY count DESC')
        print("Counts from the database:")
        for row in cursor.fetchone():
            print(row)

    except FileNotFoundError:
        print(f"File '{fname}' not found. Please check the file name and try again.")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        # Close the connection to the database
        conn.close()

# Call the function
# email_count3()
