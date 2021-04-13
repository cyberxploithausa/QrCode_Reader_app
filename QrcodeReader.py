from pyzbar.pyzbar import decode
from PIL import Image

d = decode(Image.open("Sample.png"))  #Image must be in the same folder with code or specify the path
print(d[0].data.decode())