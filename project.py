from PIL import Image

image = Image.open('IMG_2726.JPG')

image.show()
new_image = image.resize((150,150))
new_image.save('newSizeImage.png')

new_image.show()
print(image.size)
