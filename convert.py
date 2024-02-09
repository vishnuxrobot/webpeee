from PIL import Image
import os
from tqdm import tqdm

print("""

 __      __      ___.                                
/  \    /  \ ____\_ |__ ______   ____   ____   ____  
\   \/\/   // __ \| __ \\____ \_/ __ \_/ __ \_/ __ \ 
 \        /\  ___/| \_\ \  |_> >  ___/\  ___/\  ___/ 
  \__/\  /  \___  >___  /   __/ \___  >\___  >\___  >
       \/       \/    \/|__|        \/     \/     \/ 
  
                                                                      
""")
print("Designed by VishnuXrobot | Riglabs Collective.")

input_folder = 'images'
output_folder = 'webp_images'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

files = os.listdir(input_folder)
files = [f for f in files if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.PNG')]

for filename in tqdm(files, desc="Converting images"):
    image = Image.open(os.path.join(input_folder, filename))
    clean_name = os.path.splitext(filename)[0]
    webp_filename = f'{clean_name}.webp'
    webp_path = os.path.join(output_folder, webp_filename)
    image.save(webp_path, 'webp')

print('Images converted to Webp!')
