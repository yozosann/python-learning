from PIL import Image
mark = Image.open("mark.png")
im = Image.open("timg.jpeg")
layer = Image.new('RGBA', im.size, (0,0,0,0))
layer.paste(mark, (im.size[0]-150,im.size[1]-60))
out = Image.composite(layer,im,layer)
out.save('result.jpg', 'jpeg')