import socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(('yonasnegese.netlify.app.com',80))
cmd = 'GET http://yonasnegese.netlify.app.com HTTP/1.1\n\n'.encode()
mySocket.send(cmd)

# while True:
#     data = mySocket.recv(500)
#     if(len(data) < 1):
#         break
#     print(data.decode())
# mySocket.close()


# **********
# newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# newSocket.connect(('data.pr4e.org', 80))

# Correctly formatted HTTP GET request with the Host header
# cmd2 = 'GET /intro-short.txt HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n'.encode()
# newSocket.send(cmd2)

# while True:
    # data = newSocket.recv(500)
    # if len(data) < 1:
    #     break
    # # print(data.decode())

# newSocket.close()
# *****************
import urllib.request, urllib.parse, urllib.error
import re
url = ' http://py4e-data.dr-chuck.net/comments_2117127.html '
response = urllib.request.urlopen(url)
html = response.read()
decodedHtml = html.decode()
lines = decodedHtml.splitlines()
total_sum = 0
for line in lines:
    if line.startswith('<tr>'):
        match = re.search(r'([0-9]+)',line)
        if match:
            total_sum += int(match.group())
# print(total_sum)

import urllib.request
from bs4 import BeautifulSoup

# Parameters for the problem
start_url = "http://py4e-data.dr-chuck.net/known_by_Tasha.html"
position = 18  # Position in the list (1-based indexing)
repeat = 7     # Number of times to repeat the process

# Current URL to process
current_url = start_url

# Repeat the process the specified number of times
for i in range(repeat):
    print(f"Retrieving: {current_url}")
    # Fetch and parse the HTML
    response = urllib.request.urlopen(current_url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    # Find all anchor tags
    links = soup.find_all('a')

    # Get the link at the specified position
    target_link = links[position - 1]  # Convert 1-based index to 0-based index
    current_url = target_link.get('href')  # Update the URL for the next iteration

# Print the last name retrieved
last_name = current_url.split('_')[-1].split('.')[0]
# print(f"Last name in sequence: {last_name}")
