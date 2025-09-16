import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import pandas as pd
import qrcode

# Configurations
# template_path = "template/nexus_template_2025.jpg"
input_data_path = 'csv_data/nexus.csv'
result_path = "result"

# template = cv2.imread(template_path)
template_member = cv2.imread("template/nexus/member.png")
template_kids_blue = cv2.imread("template/nexus/kids_blue.png")
template_kids_pink = cv2.imread("template/nexus/kids_pink.png")
template_pastor = cv2.imread("template/nexus/pastor.png")

print("template_member shape:", template_member.shape)
print("template_kids_blue shape:", template_kids_blue.shape)
print("template_kids_pink shape:", template_kids_pink.shape)
print("template_pastor shape:", template_pastor.shape)

h = template_member.shape[0]
w = template_member.shape[1]

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
    if(df['type'][i] == 'member'):
        img = template_member.copy()
    elif(df['type'][i] == 'kids_blue'):
        img = template_kids_blue.copy()
    elif(df['type'][i] == 'kids_pink'):
        img = template_kids_pink.copy()
    elif(df['type'][i] == 'pastor'):
        img = template_pastor.copy()
    else:
        print("Unknown type:", df['type'][i])
        continue
    fontpath = "font/supermarket/supermarket-1-1/supermarket.ttf"
    font = ImageFont.truetype(fontpath, 250, encoding='utf-8')

    img_pil = Image.fromarray(img)

    # Name
    draw = ImageDraw.Draw(img_pil)
    printToText(draw, df['name'][i], font, w / 2, 900, color=(255, 255, 255, 0))

    # position
    msg = str(df['position'][i])
    font = ImageFont.truetype(fontpath, 90)
    # printToText(draw, msg, font, w * 2 / 3 + 120, 1550, align="right")
    printToText(draw, msg, font, 50, 1550,align="left")

    # church
    msg = str(df['church'][i])
    font = ImageFont.truetype(fontpath, 53)
    # printToText(draw, msg, font, w * 2 / 3 + 120, 1070)
    printToText(draw, msg, font, 50, 1650,align="left")

    # id
    # msg = str(df['id'][i])
    # font = ImageFont.truetype(fontpath, 43)
    # # printToText(draw, msg, font, w * 2 / 3 + 120, 1070)
    # printToText(draw, msg, font, 50, 1720,align="left")
    msg = f"2025{str(df['id'][i]).zfill(4)}"
    font = ImageFont.truetype(fontpath, 38)
    # printToText(draw, msg, font, w * 2 / 3 + 120, 1070)
    printToText(draw, msg, font, 1025, 1770)

    res = np.array(img_pil)

    # Insert QR Code
    # qr_code_path = "qr_codes/" + str(df['qr_code_filename'][i])  # Assuming QR codes are stored in 'qr_codes' folder
    # qr_code = cv2.imread(qr_code_path, cv2.IMREAD_UNCHANGED)
    # if qr_code is not None:
    #     print("qr_shape:",qr_code.shape)
    #     print("img_shape:",res.shape)
    #     # Convert QR code to 3-channel (RGB) if it has an alpha channel
    #     if qr_code.shape[2] == 4:  # Check if the image has 4 channels (RGBA)
    #         qr_code = cv2.cvtColor(qr_code, cv2.COLOR_BGRA2BGR)

    #     qr_h, qr_w = qr_code.shape[:2]
    #     scale_factor = 2  # Scale QR code to fit the lower right corner
    #     qr_code_resized = cv2.resize(qr_code, (int(qr_w * scale_factor), int(qr_h * scale_factor)))
    #     qr_h_resized, qr_w_resized = qr_code_resized.shape[:2]
    #     x_offset = w - qr_w_resized - 50  # 50px padding from the right edge
    #     y_offset = h - qr_h_resized - 50  # 50px padding from the bottom edge
    #     print(x_offset,y_offset)
    #     res[y_offset:y_offset + qr_h_resized, x_offset:x_offset + qr_w_resized] = qr_code_resized

    qr_data = f"2025{str(df['id'][i]).zfill(4)}"
    print(str(df['id'][i]))
    qr_img = qrcode.make(qr_data)
    qr_img = qr_img.convert("RGB")
    qr_code = np.array(qr_img)
    qr_code = cv2.cvtColor(qr_code, cv2.COLOR_RGB2BGR)
    qr_h, qr_w = qr_code.shape[:2]
    scale_factor = 0.9
    qr_code_resized = cv2.resize(qr_code, (int(qr_w * scale_factor), int(qr_h * scale_factor)))

    qr_h_resized, qr_w_resized = qr_code_resized.shape[:2]
    x_offset = w - qr_w_resized - 50
    y_offset = h - qr_h_resized - 60

    res[y_offset:y_offset + qr_h_resized, x_offset:x_offset + qr_w_resized] = qr_code_resized

    
    # cv2.imwrite(result_path + "/file" + str(i).zfill(3) + ".jpg", res)
    cv2.imwrite(f"{result_path}/nametag_{str(df['id'][i]).zfill(4)}.jpg", res)