import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=4,
    border=2,
    error_correction = qrcode.constants.ERROR_CORRECT_H
)

def create_qrcode(prod, name):
    qr.add_data(prod)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(name)


prod = input("Enter the data to be displayed in the qrcode :- ")
print("Please specify the type of image file along with the file name.")
name = input("Enter the name of the file :- ")

create_qrcode(prod, name)