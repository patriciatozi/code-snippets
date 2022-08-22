from PIL import Image

file_name = "example.jpg"

with Image.open(file_name) as img:
    img.load()

# Object type: `<class 'PIL.JpegImagePlugin.JpegImageFile'>`
type(img)

img.show()

# Image object elements
img.format                  # JPEG
img.size                    # (1920, 1080)
img.mode                    # RGB

# Cropping the image and saving it in another file
cropped_img = img.crop((600, 90, 1300, 1000))
cropped_img.save("cropped_image.jpg")

# Rotate the image 45 degrees counterclockwise
rotated_img = img.rotate(45)
rotated_img.show()