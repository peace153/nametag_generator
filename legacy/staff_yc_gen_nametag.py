import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import pandas as pd

#configurations
template_path="template/staff.jpg"
input_data_path='csv_data/yfc_staff_test.csv'
result_path="result"

template = cv2.imread(template_path)

h = template.shape[0]
w = template.shape[1]

df = pd.read_csv(input_data_path,encoding='utf-8')
print(df.head())

for i in range (0,len(df)):
    print(i)
    img = template.copy()
    # fontpath = "font/Mitr/Mitr-Bold.ttf"     
    fontpath = "font/supermarket/supermarket-1-1/supermarket.ttf"
    font = ImageFont.truetype(fontpath, 250,encoding='utf-8')

    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    #name
    msg = df['nickname'][i]
    text_w, text_h = draw.textsize(msg,font=font)
    draw.text(((w-text_w)/2, (h-text_h)/3-60), msg+" " , font = font, fill = (0,0,0,0))

    #fullname
    msg = str(df['fullname'][i])
    # fontpath = "Mitr/Mitr-SemiBold.ttf"
    font = ImageFont.truetype(fontpath, 60)
    draw.text(((w)/5-120, 3*h/4-300), msg  , font = font, fill = (0,0,0,0))
    
    #category
    msg = str(df['category'][i])
    font = ImageFont.truetype(fontpath, 60)
    text_w, text_h = draw.textsize(msg,font=font)
    draw.text(((w)/5-120, 4.25*h/5-220), msg+" "  , font = font, fill = (0,0,0,0))

    #church
    msg = str(df['church'][i])
    font = ImageFont.truetype(fontpath, 60)
    text_w, text_h = draw.textsize(msg,font=font)
    draw.text(((w)/5-120, 4.25*h/5+65), msg+" "  , font = font, fill = (0,0,0,0))

    res = np.array(img_pil)
    cv2.imwrite(result_path+"/staff"+str(i).zfill(3)+".jpg", res)
    # cv2.imwrite("test.jpg",res)
    # break
# cv2.imshow("test",res)
# cv2.waitKey(0)