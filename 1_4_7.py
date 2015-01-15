import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw    

#set logo
abslogo = os.getcwd() + "\logo.png"
logo = PIL.Image.open(abslogo)
imagesdir = os.getcwd() + "\images"


def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses \images directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() + "\images" # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)            
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    open_others(image_list, file_list)
    return image_list, file_list

    

def open_image():
    # show logo
    global logo
    fig, axes = plt.subplots(1, 1)
    axes.imshow(logo, interpolation='none')
    get_images()
    
def open_others(image_list, file_list):
# Directory to save images to
    newdir = (imagesdir + "\out")
    print newdir
    fig, axes = plt.subplots(1, 1)
#    prin = 0 # Used to test if image_list is working correctly and detecting images
    for image in range(len(image_list)):
#        prin += 1 # Used to test if image_list is working correctly and detecting images
#    print prin # Used to test if image_list is working correctly and detecting images
        # Parse the filename
        new_image = image_list[image]
        filename, filetype = file_list[image].split('.')
        new_image_filename = os.path.join(newdir, filename + '.png')
#        image.paste(logo, (0, 0))
        new_image.save(new_image_filename)

    
    

    
