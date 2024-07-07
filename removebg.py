from rembg import remove
import numpy as np
from PIL import Image
from pillow_heif import register_heif_opener
import os.path


register_heif_opener()


# Load the input image
input_image = Image.open('input.jpg')

# Convert the input image to a numpy array
input_array = np.array(input_image)

# Apply background removal using rembg
output_array = remove(input_array)

# Create a PIL Image from the output array
output_image = Image.fromarray(output_array)
output_image = output_image.resize((output_image.width, output_image.height))

# Save the output image
## output_image.save('output_image.png')
################################################################

existing_image = output_image ##Image.open('output_image.png')
###bg_image = Image.open('bg_image.jpeg')


# Create a new white image with 1440x900 dimensions
#n ew_image = Image.new("RGB", (1440, 900), (255, 255, 255))

for i in range(60):
    print(i)

    if os.path.exists('.\\backgroundImage\\bg' + str(i) + '.heic'):
        bg_image = Image.open('.\\backgroundImage\\bg' + str(i) + '.heic')
    else:
        bg_image = Image.open('.\\backgroundImage\\bg' + str(i) + '.png')

    bg_image = bg_image.resize((bg_image.width // 3, bg_image.height // 3))

    # Calculate the center position for the existing image
    x = (bg_image.width - existing_image.width ) // 4
    y = (bg_image.height - existing_image.height) // 4

    # Paste the existing image onto the new white image at the center position
    bg_image.paste(existing_image, (x, y),mask = existing_image)

    # Save the new image as a PNG file
    bg_image.save('.\\output\\newImage' + str(i) + '.png')