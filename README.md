# pyBlur

`pyBlur` is a simple extension to OpenCV's `GaussianBlur`. There are times when you need to blur only a part of the image instead of blurring the entire image. `pyBlur` can blur any arbitrary shape in an image. You just need to pass the co-ordinates and it will blur the closed polygon formed by those co-ordinates. This comes in handly when you've to blur contours as you can just pass the result of `cv2.findContours` to `pyBlur`'s functions.  

When a part of an image is blurred, most of the times it is harsh on the eyes. `pyBlur` also provides a method of blurring softly such that the blurred portion blends into the image in the background.  

## Documentation 

* `pyblur.**BlurRect**(image, rect, ksize, sigmaX [, sigmaY])`  
Blurs a rectangular portion of the image defined by a numpy array `rect` which is `[x,y,width,height]`. `ksize`,`sigmaX`, and `sigmaY` mean the same as they mean in `cv2.GaussianBlur`.
* `pyblur.**BlurContours**(image, contours, ksize, sigmaX [, sigmaY])`  
Blurs arbitrary polygons defined by the contours. `ksize`,`sigmaX`, and `sigmaY` mean the same as they mean in `cv2.GaussianBlur`.
* `pyblur.**SoftBlurRect**(image, rect, ksize, sigmaX [,sigmaY [,mksize [,msigmaX [,msigmaY]]]], **kwargs)`  
Blurs a rectangular portion of the image defined by a numpy array `rect` which is `[x,y,width,height]` softly such that it blends with the background.`ksize`,`sigmaX`, and `sigmaY` are the parameters used to blur the image once using `cv2.GaussianBlur`.`mksize`,`msigmaX`, and `msigmaY` are the parameters used to blur the mask using `cv2.GaussianBlur` on successive iterations. `iters` can be passed to `kwargs` to set the number of iterations used for soft blurring.
* `pyblur.**SoftBlurContours**(image, contours, ksize, sigmaX [,sigmaY [,mksize [,msigmaX [,msigmaY]]]], **kwargs)`  
Blurs a rectangular portion of the image defined by a numpy array `rect` which is `[x,y,width,height]` softly such that it blends with the background.`ksize`,`sigmaX`, and `sigmaY` are the parameters used to blur the image once using `cv2.GaussianBlur`.`mksize`,`msigmaX`, and `msigmaY` are the parameters used to blur the mask using `cv2.GaussianBlur` on successive iterations. `iters` can be passed to `kwargs` to set the number of iterations used for soft blurring.



## Usage  

(Check samples in next section)

```python
out1 = pyblur.BlurRect(img, [500,50,100,150], 17, 5) 
# Blurs rectangle with top-left point at (500,50) and of size (100,150).
# kernel = 17x17
# sigmaX = 5
```
```python
out2 = pyblur.BlurContours(img, [[np.array([[500,50],[600,300],[150,200]])]], 17, 5)
# Blurs contours passed as [[np.array([[500,50],[600,300],[150,200]])]].
# The array consists of one polygon formed by points (500,50), (600,300), and (150,200).
# kernel = 17x17
# sigmaX = 5
```
```python
out3 = pyblur.SoftBlurRect(img, [500,50,100,150], 27, 5)
# Soft Blurs rectangle with top-left point at (500,50) and of size (100,150).
# kernel = 27x27
# sigmaX = 5
```
```python
out4 = pyblur.SoftBlurContours(img, [[np.array([[500,50],[600,300],[150,200]])],
		[np.array([[800,500],[950,500],[900,650]])]], 17, 5)
# Soft Blurs contours passed as [[np.array([[500,50],[600,300],[150,200]])]].
# The array consists of two polygons formed by points \
# [(500,50), (600,300), (150,200)]  and [(800,500),(950,500),(900,650)].
# kernel = 17x17
# sigmaX = 5
```
```python
out5 = pyblur.SoftBlurRect(img, [500,50,100,150], 27, 5, 5, 55, iters=7)
# Soft Blurs rectangle with top-left point at (500,50) and of size (100,150).
# kernel for image = 27x27
# sigmaX for image = 5
# sigmaY for image = 5
# kernel for mask = 55x55
# no. of iterations = 7
```

## Results

Input

![Input](https://github.com/abdulfatir/pyBlur/raw/master/examples/in.jpg)

Output 1
![Output 1](https://github.com/abdulfatir/pyBlur/raw/master/examples/harsh-rect.jpg)

Output 2
![Output 2](https://github.com/abdulfatir/pyBlur/raw/master/examples/harsh-contour.jpg)

Output 3
![Output 3](https://github.com/abdulfatir/pyBlur/raw/master/examples/soft-rect.jpg)

Output 4
![Output 4](https://github.com/abdulfatir/pyBlur/raw/master/examples/soft-contour.jpg)

Output 5
![Output 5](https://github.com/abdulfatir/pyBlur/raw/master/examples/soft-rect-args.jpg)
