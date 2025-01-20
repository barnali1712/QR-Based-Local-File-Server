# import necessary modules

# for implementing the HTTP Web servers
import http.server

# provides access to the BSD socket interface
import socket

# a framework for network servers
import socketserver

# to display a Web-based document to users
import webbrowser

# to generate QR code
import pyqrcode
from pyqrcode import QRCode

# convert into png format
import png

# to access operating system control
import os


# assigning the appropriate port value
PORT = 8010

# this finds the name of the computer user
user_profile = os.environ.get('USERPROFILE')

# changing the directory to access the files on the desktop
# with the help of os module
desktop = os.path.join(user_profile, 'OneDrive')
os.chdir(desktop)

# creating an HTTP request handler
Handler = http.server.SimpleHTTPRequestHandler

# returns the hostname of the system
hostname = socket.gethostname()

# finding the IP address of the PC
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
s.close()  # It's good practice to close the socket after use

# converting the IP address into the form of a QR code
# with the help of pyqrcode module
url = pyqrcode.create(IP)

# saves the QR code in the form of an svg
url.svg("myqr.svg", scale=8)

# opens the QR code image in the web browser
webbrowser.open('myqr.svg')

# creating the HTTP request and serving the folder on the specified port
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    print("Type this in your Browser:", IP)
    print("or use the QR code")
    httpd.serve_forever()