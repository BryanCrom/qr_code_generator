import pyqrcode

QRString = "bryancrombach.com"
url = pyqrcode.create(QRString)
url.png("qrcode.png", scale=5)