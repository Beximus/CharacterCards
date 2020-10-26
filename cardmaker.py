from PIL import Image,ImageDraw,ImageEnhance,ImageFont
import os, sys
import json
import textwrap

def argumentTranslate():
    args = sys.argv
    DescriptionPath = str(args[1])
    PicturePath = str(args[2])
    return DescriptionPath,PicturePath

paths = argumentTranslate()

imagepath = paths[1]
descriptionpath = paths[0]

picture = Image.open(imagepath)

with open (descriptionpath,'r') as file:
    characterdescription = file.read()

characterdescription = textwrap.wrap(characterdescription, width=50)

descriptionText = ""

for line in characterdescription:
    descriptionText = descriptionText +"\n"+line

newcard = Image.new('RGB', (2560, 1024), color = 'White')

fontt = ImageFont.truetype("RobotoSlab-VariableFont_wght.ttf", 50)

#  Image dimensions are 1024x1024 card diimensions are 3072x1536 - image is placed 
draw = ImageDraw.Draw(newcard)
draw.multiline_text((1152,128),descriptionText,font=fontt,fill=(0,0,0))
newcard.paste(picture,(0,0))
cardname = os.path.splitext(paths[0])
cardname = cardname[0]+".jpg"
newcard.save(cardname)


