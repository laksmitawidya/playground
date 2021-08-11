""" TCP

Transport Control Protocol
- Build on top of IP (Internet Protocol)
- Assumes IP might lose some data - stores and 
retransmits data if it seems to be lost
- Handles flow control using a transmit window
- Provides a nice reliable pipes

TCP Connections / Socket
endpoint of a bideroctional inter-process comunication flow
across an internet protocol based computer network such as the internet
process <- Internet -> process

TCP Port numbers
- A port is an application specific or process specific software communcations enpoint
- It allows multiple networked applications to coexist on the same server
- There is a list of well - known TCP port numbers

Common TCP Ports
- HTTP (80)
- HTTPS (43)
etc
 """

# Application Protocol
""" 
What problem do we want to solve with TCP & Python?
- Application protocols
- Mail
- World Wide Web
 """

# HTTP
""" - Dominant Application Layer Protocol on the internet
 - Invented for the web to retrieve html, images, documents, etc
 - Extends to be data in addition to documents - RSS, Web Services, etc.
 - Basic concept: make a connection, request a document, retrieve the document, close the connection
"""

# What is protocol?
""" 
- A set of rules that all parties follow so we can preduct each other's behavior
- And not bump into each other
"""

# Example
""" 
http://www.dr-chuck.com/page1.htm
http: protocol
www.dr-chuck.com: host
page1: document

Getting data from the server
- Each the user clicks the anchor tag with href
- Browser make a connection to the web server (port 80)
- Issues a GET request to GET the content of the page at specific URL
- Server returns HTML document to the browser 

Internet standards
- The standards for all internet protocoles are developed by an organization
- Internet engineering task force
- Standard are called RFCs : Request for commands
 """

import socket
import urllib.request, urllib.parse, urllib.error
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode() #cmd is bytes
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if(len(data)< 1):
        break
    print(data.decode())
mysock.close()


network = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in network:
    print(line.decode().strip())