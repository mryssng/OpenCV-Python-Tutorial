#!python3
# -*- coding: utf-8 -*-

'''
 Basic operations with image file

  * Load image : imread
  https://docs.opencv.org/master/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56

  * Image data : https://unsplash.com/photos/pEGyLHAPfVw
'''

import cv2

# Load file without imread flag
image1 = cv2.imread('images/duck.jpg')
cv2.imwrite('images/duck_out.jpg', image1)

# Load file without imread flag
image2 = cv2.imread('images/duck.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('images/duck_gray.jpg', image2)

# print()関数の引数endで開業の代わりに任意の文字列が挿入される
print('Image Size : ', end='')
print(src.shape)
