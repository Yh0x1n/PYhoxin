'''
Reto 006: Aspect ratio

Crea un programa que se encargue de calcular el aspect ratio de una
imagen a partir de una url.
- Url de ejemplo: https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
- Por ratio hacemos referencia por ejemplo a los "16:9" de una
imagen de 1920*1080px.
'''

from PIL import Image
import requests
from io import BytesIO

#Desde una url
def calc_ar(url):
    with requests.get(url, stream=True) as response:
        image = Image.open(response.raw)
        aspect_ratio = image.width / image.height
        return aspect_ratio

#Ahora desde un archivo local
def calc_ar_local(route):
    with Image.open(route) as img:
        return img.width / img.height

url = 'https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png'
route = '/home/yh0xr/Imágenes/Capturas de pantalla/paquita.png'
print(f'el aspect ratio es {calc_ar(url)}')
print(f'el aspect ratio de paquita es {calc_ar_local(route)}')