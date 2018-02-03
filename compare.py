import pylab as pl	# matplotlib's subpackage as pl for graph
import numpy as np	# use numpy library as np for array object
import cv2			# opencv-python

def histo(image):
	x, y = image.shape 				# get image size x*y, for a image with x rows and y columns
	histo = [0.0] * 256 			# Initializes a 256 array to hold the number of 
									# occurrences of each gray level
	for i in range(0, x): 			# count each pixel value(gray level) from 0 to x
		for j in range(0, y): 		# count each pixel value(gray level) from 0 to y
			histo[image[i, j]]+=1	# count the number of occurrences of each gray level
	
	return np.array(histo)			# return histogram 

img = cv2.imread('input_image.jpg') # read image

grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # convert image to grayscal
original_histo = histo(grayimg)				   # calculate original image's histogram

from histo_equal_compare import Hist_Equal #use histogram equalization algorithm
new_img = Hist_Equal(grayimg)			   # histogram equalized image
new_histo = histo(new_img)				   # new image's histogram

openCV_img = cv2.equalizeHist(grayimg) # openCV function histogram equalization
openCV_histo = histo(openCV_img)	   # opencv function's result histogram  


pl.subplot(231)					# image position 2 row, 3 column, first position
pl.imshow(grayimg)				# show image "grayimg"
pl.title('original image')		# graph title "original image"
pl.set_cmap('gray')				# show in gray scale

pl.subplot(232)					# image position 2 row, 3 column, second position
pl.imshow(new_img)				# show image "new_img"
pl.title('equalized image')		# graph title "equalized image"
pl.set_cmap('gray')				# show in gray scale

pl.subplot(233)					# image position 2 row, 3 column, third position
pl.imshow(openCV_img)			# show image "openCV_img"
pl.title('opence equalized image')	# graph title "opence equalized image"
pl.set_cmap('gray')				# show in gray scale

pl.subplot(234)					# image position 2 row, 3 column, fourth position
pl.plot(original_histo)			# show image "original_histo"
pl.title('Original histogram')	# graph title "original histogram"

pl.subplot(235)					# image position 2 row, 3 column, fifth position
pl.plot(new_histo)				# show image "new_histo"
pl.title('New histogram') 		# graph title "New histogram"

pl.subplot(236)					# image position 2 row, 3 column, sixth position
pl.plot(openCV_histo)			# show image "openCV_histo"
pl.title('openCV histogram')	# graph title "openCV histogram"

pl.show()
