# QR CODE USING LAIBARY SIMPLE QR CODE
# import qrcode as qr
# img = qr.make("https://www.youtube.com/watch?v=FOGRHBp6lvM&t=592s")
# img.save("qr.png")


import segno
qr = segno.make("https://www.youtube.com/")
qr.save("segno_image.png",scale =30,border = 4, dark = "black",light = "white")

from PIL import Image
img = Image.open("example.jpg")
img.show()