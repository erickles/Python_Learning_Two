# Before, install the modules below
# pip install pillow

from PIL import Image

mac = Image.open('ancap.jpg')

# print(mac.size)
# print(mac.format_descrption)
# mac.show()
x = 0
y = 0

w = 529 / 3
h = 532 / 10

test = mac.crop((x,y,w,h))
# test.show()

# mac.paste(im=test,box=(4,0))
# mac.show()

test2 = mac.resize((3000,500))
test2.rotate(90)
test2.save('boom.jpg')
# test2.show()

test3 = mac.rotate(90)
# test3.show()

mac.putalpha(128)
mac.show()


