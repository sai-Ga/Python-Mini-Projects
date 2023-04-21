import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("https://github.com/sai-Ga/Python-Mini-Projects/tree/main/QRCode")
qr.png("qrcode.png", scale=8)


qrdecode = decode(Image.open("qrcode.png"))
print(qrdecode[0].data.decode("utf-8"))
