from PIL import Image
import os

path = 'D:/Application/Mumu/emulator/nemu/EmulatorShell/products/yys/'


def convert_png_to_jpeg(image_path):
    im = Image.open(image_path)
    iname = image_path[0: (len(image_path) - 3)] + "jpg"
    im.save(iname, "JPEG")


for img_name in os.listdir(path):
    img_path = path + img_name
    print(img_path)
    convert_png_to_jpeg(img_name)
