import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import pandas as pd

#configurations
template_path="template/church_camp_2024/church_white.JPG"
input_data_path='csv_data/church_camp_2024/church_white.csv'
result_path="result"
file_prefix="white"

template = cv2.imread(template_path)

h = template.shape[0]
w = template.shape[1]

print("h="+str(h))
print("w="+str(w))

def printToText(draw,msg,font,target_x,target_y,align="center",color=(0,0,0,0)):
    dimension = font.getbbox(msg)
    text_w = dimension[2]-dimension[0]
    text_h = dimension[3]-dimension[1]
    # print(text_w,text_h)
    if align=="center":
        draw.text(
            (target_x-(text_w/2), target_y-(text_h/2)),
            msg+" " ,align="center",
            font = font,
            fill = color)
    else :
        draw.text(
            (target_x, target_y),
            msg+" " ,align=align,
            font = font,
            fill = color)

df = pd.read_csv(input_data_path,encoding='utf-8',dtype=object)
print(df.head())

for i in range (0,len(df)):
    print(i)
    img = template.copy()
    # fontpath = "font/Mitr/Mitr-Bold.ttf"     
    fontpath = "font/supermarket/supermarket-1-1/supermarket.ttf"
    

    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)

    msg = str(df['nickname'][i])
    font = ImageFont.truetype(fontpath, 270,encoding='utf-8')
    printToText(draw,msg,font,w/2,650)

    msg = str(df['group'][i])
    font = ImageFont.truetype(fontpath, 90)
    printToText(draw,msg,font,w/3-120,h*2/3+30)
    
    msg = str(df['family'][i])
    font = ImageFont.truetype(fontpath, 90)
    printToText(draw,msg,font,w*2/3+120,h*2/3+30)

    msg = str(df['room'][i])
    font = ImageFont.truetype(fontpath, 90)
    printToText(draw,msg,font,w/2,1720)

    res = np.array(img_pil)
    cv2.imwrite(result_path+"/"+file_prefix+str(i).zfill(3)+".jpg", res)
