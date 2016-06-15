import cv2
import numpy as np

def SoftBlurContours(image, contours, ksize, sigmaX, *args, **kwargs):
	iterations = 2
	if 'iters' in kwargs:
		iterations = kwargs['iters']
	sigmaY = args[0] if len(args) > 0 and args[0] != None else sigmaX
	imgksize = args[1] if len(args) > 1 and args[1] != None else ksize
	imgsigmaX = args[2] if len(args) > 2 and args[2] != None else sigmaX
	imgsigmaY = args[3] if len(args) > 3 and args[3] != None else imgsigmaX
	mask = np.zeros(image.shape[:2])
	for i, contour in enumerate(contours):
		cv2.drawContours(mask, contour, i, 255, -1)
	blurred_image = cv2.GaussianBlur(image, (imgksize,imgksize), imgsigmaX, None, imgsigmaY)
	result = np.copy(image)
	for _ in xrange(iterations):
		mask = cv2.GaussianBlur(mask, (ksize, ksize), sigmaX, None, sigmaY)
		alpha = mask/255.
		result = alpha[:, :, None]*blurred_image + (1-alpha)[:, :, None]*result
	return result

def SoftBlurRect(image, rect, ksize, sigmaX, *args, **kwargs):
	x,y,w,h = rect
	contours = [[np.array([[x,y],[x+w,y],[x+w,y+h],[x,y+h]])]]
	return SoftBlurContours(image, contours, ksize, sigmaX, *args, **kwargs)

def BlurContours(image, contours, ksize, sigmaX, *args):
	sigmaY = args[0] if len(args) > 0 else sigmaX
	mask = np.zeros(image.shape[:2])
	for i, contour in enumerate(contours):
		cv2.drawContours(mask, contour, i, 255, -1)
	blurred_image = cv2.GaussianBlur(image, (ksize, ksize), sigmaX, None, sigmaY)
	result = np.copy(image)
	alpha = mask/255.
	result = alpha[:, :, None]*blurred_image + (1-alpha)[:, :, None]*result
	return result

def BlurRect(image, rect, ksize, sigmaX, *args):
	x,y,w,h = rect
	contours = [[np.array([[x,y],[x+w,y],[x+w,y+h],[x,y+h]])]]
	return BlurContours(image, contours, ksize, sigmaX, *args)

img = cv2.imread('in.jpg',1)
out = BlurRect(img, [0,0,50,60], 57, 10)
cv2.imwrite('out.png', out)