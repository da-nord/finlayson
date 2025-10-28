#134 libraries
#WORKING


# 6m50 example import PIL

from PIL import Image



with Image.open('134.jpg') as img:
    # Apply effect (e.g., rotate)
    img = img.rotate(45)
    
    # Check the mode and convert to RGB if necessary
    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
        img = img.convert('RGB')
    
    # Save modified image as JPEG
    img.save('134-rotated.jpg', format='JPEG')