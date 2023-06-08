import qrcode 
import qrcode.image.svg

def qr_generator():
    qr = qrcode.QRCode(
        version= 1, 
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        border=2,
    )

    qr.add_data(f"{data}")
    qr.make(fit=True)
    img = qr.make_image()
    img.save(f"{file_name}.png")
    
    
def svg_image():
    factory = qrcode.image.svg.SvgPathImage
    svg_image = qrcode.make(f"{data}", image_factory = factory)
    svg_image.save(f'{file_name}.svg')
    


data = input("Enter the data you want to see in the qrcode :- ")
file_name = input("Enter the file name you want save with :- ")

i = input("Enter svg for .svg file or the file the will be in the .png format :- ")

if i == "svg":
    svg_image()
else:
    qr_generator()

    
    