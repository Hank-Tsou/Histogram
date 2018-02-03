import pylab as pl	# matplotlib's subpackage as pl for graph
import numpy as np	# use numpy library as np for array object
import cv2			# opencv-python

def Hist_Equal(image):				# define function histogram equalization (input image)
### count values for each pixels
	x, y = image.shape 				# get image size x*y, for a image with x rows and y columns
	histo = [0.0] * 256 			# Initializes a 256 array to hold the number of 
									# occurrences of each gray level
	for i in range(0, x): 			# count each pixel value(gray level) from 0 to x
		for j in range(0, y): 		# count each pixel value(gray level) from 0 to y
			histo[image[i, j]]+=1	# count the number of occurrences of each gray level
					
### cdf and new pixels values		
	cdf = np.cumsum(np.array(histo))						# cumulative distribution function
	trans_val = np.uint8((cdf-cdf[0])/((x*y)-cdf[0])*255)	# calculate transfer value
													
### applying transfered values for each pixels
	new_img = np.zeros_like(image) 	# Return an empty array new_img with shape and type of input.
	for i in range(0, x):			# count each pixel value(gray level) from 0 to x
		for j in range(0, y):		# count each pixel value(gray level) from 0 to y
			new_img[i, j] = trans_val[image[i, j]]	#fill the equalization result in the array
			
	return new_img					# return transformed image

### main
image_name = input('image name(with .pnh .jpg): ')  # input image name
img = cv2.imread(image_name) 						# read image 
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)		# convert image to grayscal
new_img = Hist_Equal(grayimg)						# do histogram equalization	
	
### show original and equalized image
pl.subplot(121)					# image position 1 row, 2 column, first position
pl.imshow(grayimg)				# show image "grayimg"
pl.title('original image')		# graph title "original image"
pl.set_cmap('gray')				# show in gray scale

pl.subplot(122)					# image position 1 row, 2 column, second position
pl.imshow(new_img)				# show image "grayimg"
pl.title('equalized image')		# graph title "original image"
pl.set_cmap('gray')				# show in gray scale

pl.show()						# output image
