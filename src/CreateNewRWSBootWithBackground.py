from rembg import remove
import numpy as np
from PIL import Image
from pillow_heif import register_heif_opener
import os.path
from random import randrange

register_heif_opener()
loop = 0
style = 'style3375'


arrInputDir  = os.listdir('c:\\dev\\ai\\testImage\\input-1')
for d in arrInputDir:
    style = 'c:\\dev\\ai\\testImage\\input-1\\' + d
    arrInputImageDir  = os.listdir(style)

    if arrInputImageDir.__len__() >= 5: 
        continue
    #print(arrInputDir)
    for f in arrInputImageDir:
        imageName = style + '\\' + f
        print(imageName)
        #     # Load the input image

        input_image = Image.open(imageName, 'r')

        #Convert the input image to a numpy array
        input_array = np.array(input_image)

        # Apply background removal using rembg
        output_array = remove(input_array)

        #     # Create a PIL Image from the output array
        output_image = Image.fromarray(output_array)
        output_image = output_image.resize((output_image.width*2, output_image.height*2))

        loop_range  = [-1, 0]
        for flip in loop_range:
            
            if flip == 0:
                output_image = output_image.transpose(method=flip)

            for ii in range(34):
                print(ii)
                rand = randrange(35)
                
                if os.path.exists('.\\backgroundImage\\bg' + str(rand) + '.heic'):
                    bg_image = Image.open('.\\backgroundImage\\bg' + str(rand) + '.heic')
                else:
                    bg_image = Image.open('.\\backgroundImage\\bg' + str(rand) + '.png')

                #bg_image = bg_image.transpose(method=Image.TRANSVERSE)

                bg_image = bg_image.resize((bg_image.width // 4, bg_image.height // 4))

                #output_image = output_image.resize((output_image.width * 2, output_image.height * 2))


                # Calculate the center position for the existing image
                x = bg_image.width // 4
                y = bg_image.height // 4

                if ( bg_image.width >= output_image.width or bg_image.height >= output_image.height):
                    x = (bg_image.width - output_image.width ) // 3
                    y = (bg_image.height - output_image.height) // 3
                else:
                    x = (output_image.width - bg_image.width ) // 3
                    y = (output_image.height - bg_image.height) // 3

                # Paste the existing image onto the new white image at the center position
                bg_image.paste(output_image, (x, y),mask = output_image)

                # Save the new image as a PNG file
                newImageDir = 'F:\\AIImages\\RWSBootWithbackground\\' + d
                print(newImageDir)

                if not os.path.exists(newImageDir):
                    os.makedirs(newImageDir)

                bg_image.save(newImageDir + '\\newImage' + str(loop) + '.png')
                loop = loop + 1
    

# for num in range(6):
#     # Load the input image
#     input_image = Image.open('.\\input\\' + style + '\\item-' + str(num) + '.jpeg')

#     # Convert the input image to a numpy array
#     input_array = np.array(input_image)

#     # Apply background removal using rembg
#     output_array = remove(input_array)

#     # Create a PIL Image from the output array
#     output_image = Image.fromarray(output_array)
#     output_image = output_image.resize((output_image.width, output_image.height))

   
#     loop_range  = [-1, 0]
#     for flip in loop_range:
        
#         if flip == 0:
#             output_image = output_image.transpose(method=flip)

#         for i in range(60):
#             print(i)
            
#             if os.path.exists('.\\backgroundImage\\bg' + str(i) + '.heic'):
#                 bg_image = Image.open('.\\backgroundImage\\bg' + str(i) + '.heic')
#             else:
#                 bg_image = Image.open('.\\backgroundImage\\bg' + str(i) + '.png')

#             #bg_image = bg_image.transpose(method=Image.TRANSVERSE)

#             bg_image = bg_image.resize((bg_image.width // 3, bg_image.height // 3))

#             # Calculate the center position for the existing image
#             x = (bg_image.width - output_image.width ) // 4
#             y = (bg_image.height - output_image.height) // 4

#             # Paste the existing image onto the new white image at the center position
#             bg_image.paste(output_image, (x, y),mask = output_image)

#             # Save the new image as a PNG file
#             bg_image.save('D:\\AIImages\\BootWithbackground\\' + style + '\\newImage' + str(loop) + '.png')
#             loop = loop + 1