from PIL import Image
import json

import numpy as np
import scipy.misc as smp
# from .new import toimage
from code import toimage



def convert_to_ion(img_path):
    im = Image.open(img_path)
    pix = im.load()
    length,height = im.size

    ion = []

    for i in range(length):
        for j in range(height):
            r,g,b = pix[i,j]

            ion_data = {
                "r": r,
                "g": g,
                "b": b,
                "location":(i,j)
            }

            ion.append(ion_data)
    fin_data = {
        "height": height,
        "length": length,
        "img": ion
    }
    with open('gta.json', 'w') as fp:
        json.dump(fin_data, fp)

def convert_to_img(json_path):
    f = open(json_path) 
    json_data = json.load(f) 
    data = np.zeros((json_data["height"],json_data["length"],3), dtype=np.uint8)

    for i in range(0,len(json_data["img"])):
        length = json_data["img"][i]["location"][0]
        height = json_data["img"][i]["location"][1]
        r = json_data["img"][i]["r"]
        g = json_data["img"][i]["g"]
        b = json_data["img"][i]["b"]
        data[height,length] = [r,g,b]
    img = toimage( data ) 
    img.show()



# convert_to_ion("./gta.jpg")
convert_to_img('./gta.json')
    
