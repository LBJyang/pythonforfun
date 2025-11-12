from PIL import Image

im = Image.open("test.jpg")
w, h = im.size
print(f"Original image size:{w} * {h}")
im.thumbnail((w // 2, h // 2))
print(f"Resize image to:{w//2} * {h//2}")
im.save("thumbnail.jpg", "jpeg")
