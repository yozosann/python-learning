from PIL import Image

im = Image.open('tokyo.jpg')

w,h = im.size
print('Original image size: %sx%s' % (w, h))

# 缩放到%：
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))

im.save('thumbnail.jpg', 'jpeg')