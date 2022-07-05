import os, cairo
from PIL import Image, ImageEnhance, ImageDraw, ImageFont, ImageFilter

foto = Image.open("foto.jpg")
krop = Image.open("krop.png")
krop.thumbnail((10, 10))

foto_szare = foto.convert('L')
m = 5
plik = 'rysunek.png'
n = 600
powierzchnia = cairo.ImageSurface(cairo.FORMAT_RGB24, n, n)
kontekst = cairo.Context(powierzchnia)
# Ustawiamy kolor (tła)
kontekst.set_source_rgb(255, 255, 255)
# Wypełniamy obszar rysunku wybranym kolorem
kontekst.paint()
x = 1
kontekst.set_source_rgb(0, 0, 0)
#podzielenie obrazu
for i in range(n // m):
    for j in range(n // m):
        wycinek = (j * m, i * m, j * m + m, i * m + m)
        foto_wycinek = foto_szare.crop(wycinek)
        roz = foto_wycinek.filter(ImageFilter.GaussianBlur(20))
        pix = roz.load()
        a = pix[1, 1]
        if a <= 255 and a > 227:
            kontekst.set_line_width(m * 0.16)
        elif a <= 227 and a > 199:
            kontekst.set_line_width(m * 0.24)
        elif a <= 199 and a > 171:
            kontekst.set_line_width(m * 0.32)
        elif a <= 171 and a > 143:
            kontekst.set_line_width(m * 0.4)
        elif a <= 143 and a > 115:
            kontekst.set_line_width(m * 0.48)
        elif a <= 115 and a > 87:
            kontekst.set_line_width(m * 0.56)
        elif a <= 87 and a > 59:
            kontekst.set_line_width(m * 0.64)
        elif a <= 59 and a > 31:
            kontekst.set_line_width(m * 0.72)
        elif a <= 31 and a >= 0:
            kontekst.set_line_width(m * 0.8)
        kontekst.move_to(j * m, i * m)
        kontekst.line_to(j * m + m, i * m + m)
        kontekst.stroke()
powierzchnia.write_to_png(plik)
