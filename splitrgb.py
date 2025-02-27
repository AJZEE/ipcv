from PIL import Image

img = Image.open(r"tree.jpg")
r, g, b = img.split()
len(r.histogram())
### 256 ###

r.histogram()
