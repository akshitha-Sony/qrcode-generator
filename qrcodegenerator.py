import qrcode
import image
qr = qrcode.QRCode(
    version = 15, # 15 means the version of the QRCode, higher the number, bigger the code and complicated picture
    box_size=10, # size of the box where QRCode will be displayed
    border=5 # White part of the image, --border on all 4 sides with white colour
)

data = "https://www.youtube.com/watch?v=dr7z7a_8lQw&list=PLKnIA16_Rmvbr7zKYQuBfsVkjoLcJgxHH&index=13&ab_channel=CampusX"

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color = 'white')
img.save("test.png")


