# importing needed modules
import sys
import os
from PIL import Image

# to use, in the terminal write "python jpg_to_png_converter.py <old_folder_name> <new_folder_name>"
old_folder_name = str(sys.argv[1])
new_folder_name = str(sys.argv[2])

#checking if directory already exists
does_exist = os.path.exists(rf'{new_folder_name}')

#creating one if it does not
if does_exist == False:
    os.mkdir(rf'{new_folder_name}')

#converting the images
for photo in os.listdir(rf'{old_folder_name}'):
    img = Image.open(rf'{old_folder_name}\{photo}')
    '''
    can use lines 23 & 24 or line 26, but not both, will cause duplicates
    '''
    clean_name = os.path.splitext(photo)[0]
    img.save(f'{new_folder_name}\{clean_name}.png','png')
    #or, can only run one at a time
    img.save(rf'{new_folder_name}\{photo}'.replace('.jpg', '.png'), 'png')
    