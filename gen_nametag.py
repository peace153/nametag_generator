import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import pandas as pd

template = cv2.imread("template/ygcf_template.jpg")

h = template.shape[0]
w = template.shape[1]

df = pd.read_csv('csv_data/ygcf.csv',encoding='utf-8')
print(df.head())

print(df['status'].unique())

for i in range (0,len(df)):
    print(i)
    img = template.copy()
    # fontpath = "font/Mitr/Mitr-Bold.ttf"     
    fontpath = "font/supermarket/supermarket-1-1/supermarket.ttf"
    font = ImageFont.truetype(fontpath, 250,encoding='utf-8')

    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    #name
    msg = df['name'][i]
    text_w, text_h = draw.textsize(msg,font=font)
    draw.text(((w-text_w)/2, (h-text_h)/3+50), msg+" " , font = font, fill = (0,0,0,0))

    #position
    msg = str(df['position'][i])
    msg2 = ""
    # fontpath = "Mitr/Mitr-SemiBold.ttf"
    font = ImageFont.truetype(fontpath, 40)
    text_w, text_h = draw.textsize(msg,font=font)
    # print(text_w)
    if text_w > 480:
        msg_list = msg.split(" ",1)
        msg = msg_list[0]
        msg2 = msg_list[1]
    draw.text(((w)/5-120, 3*h/4-200), msg+" "  , font = font, fill = (0,0,0,0))
    draw.text(((w)/5-120, 3*h/4-200+text_h+50), msg2+" "  , font = font, fill = (0,0,0,0))


    #relation
    msg = str(df['status'][i])
    font = ImageFont.truetype(fontpath, 45)
    text_w, text_h = draw.textsize(msg,font=font)
    draw.text(((w)/5-120, 4.25*h/5-120), msg+" "  , font = font, fill = (0,0,0,0))
    #group-room
    msg = str(df['group'][i])+"/"+str(df['room'][i])
    font = ImageFont.truetype(fontpath, 50)
    text_w, text_h = draw.textsize(msg,font=font)
    draw.text(((w)/5-120, 4.25*h/5+120), msg+" "  , font = font, fill = (0,0,0,0))

    res = np.array(img_pil)
    cv2.imwrite("result/msg"+str(i)+".jpg", res)
    # cv2.imwrite("test.jpg",res)
    # break
# cv2.imshow("test",res)
# cv2.waitKey(0)