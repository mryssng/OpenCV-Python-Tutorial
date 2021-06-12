#!python3
# -*- coding: utf-8 -*-

'''
 Basic operations with image file

  * Load image : imwrite
  https://docs.opencv.org/master/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56

  * Image data : https://unsplash.com/photos/VTvnoNBowZs
'''

import cv2

# Read file
image = cv2.imread('images/duck.jpg')

# Write file as JPEG
result = cv2.imwrite('images/duck_out.jpg', image)

# Write file with Japanese file name
result = cv2.imwrite('画像フォルダ/あひる出力.jpg', image)

# Write file as PNG
result = cv2.imwrite('images/duck_out.png', image)

# Write file as worst quality JPEG
result = cv2.imwrite('images/duck_worst.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 0])

# Write file as progressive JPEG
result = cv2.imwrite('images/duck_progressive.jpg', image, [cv2.IMWRITE_JPEG_PROGRESSIVE, True])

# Write file as optimized JPEG
result = cv2.imwrite('images/duck_optimize.jpg', image, [cv2.IMWRITE_JPEG_OPTIMIZE, True])

# Write file as JPEG luma=100
result = cv2.imwrite('images/duck_luma_max.jpg', image, [cv2.IMWRITE_JPEG_LUMA_QUALITY, 100])

# Write file as JPEG chroma=100
result = cv2.imwrite('images/duck_chroma_max.jpg', image, [cv2.IMWRITE_JPEG_CHROMA_QUALITY, 100])

# Write file as PNG compression=9
result = cv2.imwrite('images/duck_comp_max.png', image, [cv2.IMWRITE_PNG_COMPRESSION, 9])
