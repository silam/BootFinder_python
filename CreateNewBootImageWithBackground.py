from rembg import remove
import numpy as np
from PIL import Image
from pillow_heif import register_heif_opener
import os.path


register_heif_opener()
loop = 0
style = 'style3375'
for num in range(6):
    # Load the input image
    input_image = Image.open('.\\input\\' + style + '\\shoe' + str(num) + '.jpg')

    # Convert the input image to a numpy array
    input_array = np.array(input_image)

    # Apply background removal using rembg
    output_array = remove(input_array)

    # Create a PIL Image from the output array
    output_image = Image.fromarray(output_array)
    output_image = output_image.resize((output_image.width, output_image.height))

    # method – Possible values of method are
    # PIL.Image.FLIP_LEFT_RIGHT = 0
    # PIL.Image.FLIP_TOP_BOTTOM
    # PIL.Image.ROTATE_90
    # PIL.Image.ROTATE_180
    # PIL.Image.ROTATE_270
    # PIL.Image.TRANSPOSE or PIL.Image.TRANSVERSE.


    loop_range  = [-1, 0]
    for flip in loop_range:
        
        if flip == 0:
            output_image = output_image.transpose(method=flip)

        for i in range(60):
            print(i)
            
            if os.path.exists('.\\backgroundImage\\bg' + str(i) + '.heic'):
                bg_image = Image.open('.\\backgroundImage\\bg' + str(i) + '.heic')
            else:
                bg_image = Image.open('.\\backgroundImage\\bg' + str(i) + '.png')

            #bg_image = bg_image.transpose(method=Image.TRANSVERSE)

            bg_image = bg_image.resize((bg_image.width // 3, bg_image.height // 3))

            # Calculate the center position for the existing image
            x = (bg_image.width - output_image.width ) // 4
            y = (bg_image.height - output_image.height) // 4

            # Paste the existing image onto the new white image at the center position
            bg_image.paste(output_image, (x, y),mask = output_image)

            # Save the new image as a PNG file
            bg_image.save('.\\output\\' + style + '\\newImage' + str(loop) + '.png')
            loop = loop + 1