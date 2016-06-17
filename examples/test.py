import pyblur
import cv2
import numpy as np

def main():
	img = cv2.imread("in.jpg")
	out1 = pyblur.BlurRect(img, [500,50,100,150], 17, 5)
	out2 = pyblur.BlurContours(img, [[np.array([[500,50],[600,300],[150,200]])]], 17, 5)
	out3 = pyblur.SoftBlurRect(img, [500,50,100,150], 27, 5)
	out4 = pyblur.SoftBlurContours(img, [[np.array([[500,50],[600,300],[150,200]])],
		[np.array([[800,500],[950,500],[900,650]])]], 17, 5)
	out5 = pyblur.SoftBlurRect(img, [500,50,100,150], 27, 5, 5, 55, iters=7)

	cv2.imwrite('harsh-rect.jpg', out1)
	cv2.imwrite('harsh-contour.jpg', out2)
	cv2.imwrite('soft-rect.jpg', out3)
	cv2.imwrite('soft-contour.jpg', out4)
	cv2.imwrite('soft-rect-args.jpg', out5)


if __name__ == '__main__':
	main()