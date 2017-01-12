from PIL import Image                                                            
import numpy                                                                     
import matplotlib.pyplot as plt                                                  
import glob

imageFolderPath = 'img/'
imagePath = glob.glob(imageFolderPath+'/*.JPG') 

im_array = numpy.array( [numpy.array(Image.open(imagePath[i]).convert('L'), 'f') for i in range(len(imagePath))] )

print(im_array)
print(im_array.shape)
print(len(im_array))