from PIL import Image

img = Image.open("DSC_0071.JPG")
print(img.size)
print(img.format)

area = (1, 320, 3649, 2990)
cropped = img.crop(area)
cropped.save("cropped.jpg")
new = Image.open("cropped.jpg")
new.show()
