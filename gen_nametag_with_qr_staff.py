import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import pandas as pd
import qrcode

# Configurations
# template_path = "template/nexus_template_2025.jpg"
input_data_path = 'csv_data/nexus_staff.csv'
result_path = "result"

# template = cv2.imread(template_path)
template_staff = cv2.imread("template/nexus/staff02.png")
template_head = cv2.imread("template/nexus/head.png")


h = template_staff.shape[0]
w = template_staff.shape[1]

def printToText(draw, msg, font, target_x, target_y, align="center", color=(0, 0, 0, 0)):
    dimension = font.getbbox(msg)
    text_w = dimension[2] - dimension[0]
    text_h = dimension[3] - dimension[1]
    if align == "center":
        draw.text(
            (target_x - (text_w / 2), target_y - (text_h / 2)),
            msg + " ", align="center",
            font=font,
            fill=color)
    else:
        draw.text(
            (target_x, target_y),
            msg + " ", align=align,
            font=font,
            fill=color)

df = pd.read_csv(input_data_path, encoding='utf-8')
df = df.fillna('')

print(df.head())

for i in range(len(df)):
    print(i)
    # img = template.copy()
    if(df['type'][i] == 'Staff'):
        img = template_staff.copy()
    elif(df['type'][i] == 'Head'):
        img = template_head.copy()
    else:
        print("Unknown type:", df['type'][i])
        continue
    fontpath = "font/supermarket/supermarket-1-1/supermarket.ttf"
    font = ImageFont.truetype(fontpath, 250, encoding='utf-8')

    img_pil = Image.fromarray(img)

    # Position
    draw = ImageDraw.Draw(img_pil)
    printToText(draw, df['position'][i], font, w / 2, 900)

    # group
    msg = str(df['group'][i])
    font = ImageFont.truetype(fontpath, 120)
    # printToText(draw, msg, font, w * 2 / 3 + 120, 1550, align="right")
    printToText(draw, msg, font, w/2, 1580)

    # name
    msg = str(df['name'][i])
    font = ImageFont.truetype(fontpath, 90)
    # printToText(draw, msg, font, w * 2 / 3 + 120, 1070)
    printToText(draw, msg, font, w/2, 1685)

    # id
    # msg = str(df['id'][i])
    # font = ImageFont.truetype(fontpath, 43)
    # # printToText(draw, msg, font, w * 2 / 3 + 120, 1070)
    # printToText(draw, msg, font, 50, 1720,align="left")
    msg = str(df['id'][i])
    font = ImageFont.truetype(fontpath, 50)
    # printToText(draw, msg, font, w * 2 / 3 + 120, 1070)
    printToText(draw, msg, font, w/2, 1750)

    res = np.array(img_pil)


    
    # cv2.imwrite(result_path + "/file" + str(i).zfill(3) + ".jpg", res)
    cv2.imwrite(f"{result_path}/staff_{str(df['id'][i])}.jpg", res)