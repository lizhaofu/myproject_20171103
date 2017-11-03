from PIL import Image
'''
print(ImageColor.getcolor('red','RGBA'))
print(ImageColor.getcolor('black','RGB'))
'''

im_path = r"data\1.jpg"
im = Image.open(im_path)
width, height = im.size
print(im.size, width, height)
print(im.format, im.format_description)
im.save(r"data\1_copy.jpg")
im.show()

'''
newIm = Image.new('RGB', (100,100),'red')
newIm.save(r"data\1.png")
newIm.show()
'''

cropedIm = im.crop((100,100,150,250))
cropedIm.save(r"data\2.png")
cropedIm.show()
crop_width, crop_height = cropedIm.size
copyIm = im.copy()


im.rotate(90).show()






