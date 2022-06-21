import sys
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


##pip instalar pillow

print("Output from Python")
print("Nome: " + sys.argv[1])
print("Cargo: " + sys.argv[2])
print("Tel: " + sys.argv[3])

nome = sys.argv[1]
cargo = sys.argv[2]
telefone = sys.argv[3]

img = Image.open("modelVazio.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Ubuntu-B.ttf", 60)
font2 = ImageFont.truetype("Ubuntu-R.ttf", 30)
font3 = ImageFont.truetype("Ubuntu-B.ttf", 40)
draw.text((770, 50), nome, (255, 255, 255), font=font)
draw.text((805, 149), cargo, (255, 255, 255), font=font2)
draw.text((893, 250), telefone, (255, 255, 255), font=font3)
img.save(nome+'.png')
