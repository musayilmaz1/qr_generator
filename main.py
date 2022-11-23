
import sys
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)
print("url giriniz")


def olustur(deger):
    if len(str(deger)) == 0:
        print("herhangi birsey yazmadiniz.")
        sys.exit()
    qr.add_data(deger)

    qr.make(fit=True)
    img = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
    img.save("qr.jpg")
    qr.clear()
    print("selam")



