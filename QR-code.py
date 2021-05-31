import pyqrcode
from pyqrcode import QRCode

#string which represent the QR code 
s = 'https://youtu.be/KnCWWkot-AM'

#Generate QR code
url = pyqrcode.create(s)

#create and save the png file "myqr.png"
url.svg('myyoutube.svg', scale=8)
