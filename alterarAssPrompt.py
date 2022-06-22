from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import shutil
import os
import datetime 
import sys
# import base64

# pip install  PyQt5

# nome = input('Nome:  ')
# cargo = 'Paralegal'
# # cargo = input('Cargo: ')
# # telefone = input('Telefone:')
# telefone = '3041-8850'

# img = Image.open("modelVazio.png")
# draw = ImageDraw.Draw(img)
# font = ImageFont.truetype("Ubuntu-B.ttf", 60)
# font2 = ImageFont.truetype("Ubuntu-R.ttf", 30)
# font3 = ImageFont.truetype("Ubuntu-B.ttf", 40)
# draw.text((770, 50), nome, (255, 255, 255), font=font)
# draw.text((805, 149), cargo, (255, 255, 255), font=font2)
# draw.text((893, 250), telefone, (255, 255, 255), font=font3)
# img.save(nome+'.png')

n = 0

while n != 'n':
    #RECEBE O NOME E CORRIGE PARA O PADRÃO DE PRIMEIRA LETRA MAISCULA
    nome = input('Nome:  ')
    nome = nome.title();
    #RECEBE O CARGO E CORRIGE PARA O PADRÃO DE PRIMEIRA LETRA MAISCULA
    cargo = input('Cargo:  ')
    cargo = cargo.title();
    #RECEBE O TELEFONE
    telefone = input('Telefone: ')
    #RECEBE O MODELO DA IMAGEM A SER ALTERADO
    img = Image.open("modelVazio.png")
    #RECEBE A IMAGEM A SER ALTERADA
    draw = ImageDraw.Draw(img)
    #RECEBE A FONTE E O TAMANHO A SER USADO
    font = ImageFont.truetype("Ubuntu-B.ttf", 60)
    font2 = ImageFont.truetype("Ubuntu-R.ttf", 30)
    font3 = ImageFont.truetype("Ubuntu-B.ttf", 40)
    #RECEBE A FONTE, POSICAO, COR A SER USADA E ESCREVE NA IMAGEM
    draw.text((770, 50), nome, (255, 255, 255), font=font)
    draw.text((805, 149), cargo, (255, 255, 255), font=font2)
    draw.text((893, 250), telefone, (255, 255, 255), font=font3)
    #SALVA IMAGEM NO CAMINHO LOCAL
    img.save(nome+'.png')

    #RECEBE A DATA DO MOMENTO
    current_time = datetime.datetime.now() 
    year = current_time.year
    month = current_time.month
    day = current_time.day
    
    #CRIA VARIAVEL COM O CAMINHO EM BASE DA DATA DE CRIACAO
    dir='./'+str(year)+'/'+str(month)+'/'+str(day)

    #VERIFICAR A EXSITENCIA DO DIRETORIO
    if os.path.isdir(dir):
        print("O diretório existe!")
    else:
        os.makedirs(dir)
        print("Diretório criado!")

    #MOVE PARA O DIRETORIO
    shutil.move(nome+'.png',dir)
    print("Arquivo movido com sucesso para diretório!")


    # converter em string
    # with open(nome+'.png', "rb") as image2string:
    #     converted_string = base64.b64encode(image2string.read())
    # print(converted_string)
    # with open(nome+'.bin', "wb") as file:
        # file.write(converted_string)

    # convertendo de string para imagem
    # file = open('encode.bin', 'rb')
    # byte = file.read()
    # file.close()

    # decodeit = open(nome+' convertido-de-string.png', 'wb')
    # decodeit.write(base64.b64decode((byte)))
    # decodeit.close()

    #QUESTIONA SOBRE A CONTINUIDADE DENTRO DO SCRIPT
    n = input('Para parar digite n ou ctrl + c: ')
else:
    print("Obrigado por usar o gerador de assinatura! ")
