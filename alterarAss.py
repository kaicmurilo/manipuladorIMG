from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


arquivo = open("nomeAss.txt", "r")


print(arquivo.readlines())

nome = input('Nome:  ')
cargo = input('Cargo: ')
telefone = input('Telefone:')

img = Image.open("modelVazio.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Ubuntu-B.ttf", 60)
font2 = ImageFont.truetype("Ubuntu-R.ttf", 30)
font3 = ImageFont.truetype("Ubuntu-B.ttf", 40)
draw.text((770, 50), nome, (255, 255, 255), font=font)
draw.text((805, 149), cargo, (255, 255, 255), font=font2)
draw.text((893, 250), telefone, (255, 255, 255), font=font3)
img.save(nome+'.png')
