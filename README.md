# nametag_generator
This is sample of python code to read .csv file and put it on picture, useful for generating conference nametag.

## setting up 

dependency : 
```python
pip install opencv-python
pip install Pillow
pip install numpy
pip install pandas
```

Put template image in template folder, put data in csv_data folder.

create result folder for storing result images

Edit the code in gen_nametag.py to correct template & data.

If you want to switch font, put the font in the font folder & edit code.

Please note that some font will have problem with text in the upper & lower layer in some language

## usage
for python 2
```
python gen_nametag.py
```
for python 3 
```
python3 gen_nametag.py
```

### todo
- put file location as a config file or variable on top of code for editing purpose.

### legacy
1.0 - PIL obsolete function draw.textsize, we must switch to use font.getbbox(msg) instead.