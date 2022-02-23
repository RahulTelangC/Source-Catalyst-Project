import cv2
img_loc = "" #add image location
filename = '' # add your jpg file

img = cv2.imread(img_loc+filename)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

inverted_gray_img = 255 - gray_img
blurred_img = cv2.GaussianBlur(inverted_gray_img, (21,21), 0)

inverterd_blurred_img = 255 - blurred_img
pencil_sketch_img = cv2.divide(gray_img, inverterd_blurred_img, scale=256.0)

cv2.imshow('original image', img)
cv2.imshow('Gray image', pencil_sketch_img)

cv2.waitKey()


