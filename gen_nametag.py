import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import pandas as pd

#configurations
template_path="template/member.jpg"
input_data_path='csv_data/yfc_test.csv'
result_path="result"

template = cv2.imread(template_path)

h = template.shape[0]
w = template.shape[1]

def printToText(draw,msg,font,target_x,target_y,align="center"):
    dimension = font.getbbox(msg)
    text_w = dimension[2]-dimension[0]
    text_h = dimension[3]-dimension[1]
    # print(text_w,text_h)
    if align=="center":
        draw.text(
            (target_x-(text_w/2), target_y-(text_h/2)),
            msg+" " ,align="center",
            font = font,
            fill = (0,0,0,0))
    else :
        draw.text(
            (target_x, target_y),
            msg+" " ,align=align,
            font = font,
            fill = (0,0,0,0))

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
    printToText(draw,df['nickname'][i],font,w/2,500)
    #name
    # msg = df['nickname'][i]
    # dimension = font.getbbox(msg)
    # text_w = dimension[2]-dimension[0]
    # text_h = dimension[3]-dimension[1]
    # print(text_w,text_h)
    # draw.text(((w-text_w)/2, (h-text_h)/3-60), msg+" " , font = font, fill = (0,0,0,0))

    # #fullname
    msg = str(df['fullname'][i])
    # # fontpath = "Mitr/Mitr-SemiBold.ttf"
    font = ImageFont.truetype(fontpath, 60)
    printToText(draw,msg,font,w/3,1080)
    #draw.text(((w)/5-120, 3*h/4-300), msg  , font = font, fill = (0,0,0,0))
    
    # #y_id
    msg = str(df['y_id'][i])
    font = ImageFont.truetype(fontpath, 60)
    printToText(draw,msg,font,w*2/3+120,1070)
    # draw.text((4*(w)/5-160, 3*h/4-300), msg+" "  , font = font, fill = (0,0,0,0))


    # #church
    msg = str(df['church'][i])
    font = ImageFont.truetype(fontpath, 60)
    printToText(draw,msg,font,w/3+10,1340)
    # text_w, text_h = draw.textsize(msg,font=font)
    # draw.text(((w)/5-120, 4.25*h/5-220), msg+" "  , font = font, fill = (0,0,0,0))

    # #workshop_1
    msg = str(df['workshop_1'][i])
    font = ImageFont.truetype(fontpath, 40)
    printToText(draw,msg,font,w/4+30,1620)
    # text_w, text_h = draw.textsize(msg,font=font)
    # draw.text(((w)/5-120, 4.25*h/5+65), msg+" "  , font = font, fill = (0,0,0,0))

    # #workshop_2
    msg = str(df['workshop_2'][i])
    font = ImageFont.truetype(fontpath, 40)
    printToText(draw,msg,font,w*3/4-30,1620)
    # text_w, text_h = draw.textsize(msg,font=font)
    # draw.text((4*(w)/5-310, 4.25*h/5+65), msg+" "  , font = font, fill = (0,0,0,0))

    res = np.array(img_pil)
    cv2.imwrite(result_path+"/file"+str(i).zfill(3)+".jpg", res)
    
    # cv2.imwrite("test.jpg",res)
    # break
# cv2.imshow("test",res)
# cv2.waitKey(0)