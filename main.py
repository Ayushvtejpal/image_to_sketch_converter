# Python program to Convert Image into sketch


# import all the required modules
import numpy as np
import imageio
import scipy.ndimage
import cv2


# take image input and assign variable to it
img = "https://media.geeksforgeeks.org/wp-content/uploads/20200910185931/input2-300x295.jpg"


# function to convert image into sketch
def rgb2gray(rgb):
	# 2 dimensional array to convert image to sketch
	return np.dot(rgb[..., :3], [0.299, 0.587, .114])


def dodge(front, back):
	final_sketch = front*255/(255-back)
	final_sketch[final_sketch > 255] = 255
	final_sketch[back == 255] = 255
	return final_sketch.astype('uint8')
ss = imageio.imread(img)
gray = rgb2gray(ss)
i = 255-gray
blur = scipy.ndimage.filters.gaussian_filter(i, sigma=13)
r = dodge(blur, gray)
cv2.imshow('image',r)
cv2.waitKey()
cv2.imwrite('4.png', r)