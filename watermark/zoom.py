from PIL import Image
im = Image.open('./mark.png')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//4, h//4))
print('Resize image to: %sx%s' % (w//4, h//4))
# 把缩放后的图像用jpeg格式保存:
im.save('mark.png', 'png')