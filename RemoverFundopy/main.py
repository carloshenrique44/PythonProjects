from rembg import remove
from PIL import Image
input_path = 'rsq3.jpg'
output_path = 'output.png'
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)