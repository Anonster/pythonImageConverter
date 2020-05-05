import sys
import os
from PIL import Image
input_path = sys.argv[1]
output_path = sys.argv[2]
extension = sys.argv[3]


if not os.path.exists(output_path):
    os.makedirs(output_path)


for filename in os.listdir(input_path):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{input_path}/{filename}')
    img.save(f'{output_path}\\{clean_name}.{sys.argv[3]}', f'{sys.argv[3]}')

print('Porcess Done')
