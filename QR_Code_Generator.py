import qrcode


data = input('Enter your text or url: ').strip()
filename = input('Enter the file name: (.jpg) ').strip()

qr = qrcode.QRCode(box_size=10, 
              border=4)
qr.add_data(data)
img = qr.make_image(fill_color='black',
              back_color='white')
img.save(filename)

print(f'qr code save as {filename}')