import cv2
# read a color image file for animal tiger
image = cv2.imread('./images/tiger.jpg')
print("Shape of given color image")
print(image.shape)
# filter to convert color tiger image to gray one
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print("Shape of converted to gray image")
print(gray_image.shape)
# write the gray image to a file
cv2.imwrite('./images/tiger_gray.jpg', gray_image)