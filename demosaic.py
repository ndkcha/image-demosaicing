import cv2
import numpy as np

img = cv2.imread("images/oldwell_mosaic.bmp")
b, g, r = cv2.split(img)

height = img.shape[1]
width = img.shape[0]

mask_blue = np.zeros((width, height), dtype=np.uint8)
mask_blue[:, ::2] = 1
mask_blue[1::2] = 0

kernel_blue = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) / 3
after_mask_blue = cv2.bitwise_and(b, b, mask=mask_blue)
filtered_blue = cv2.filter2D(after_mask_blue, -1, kernel_blue)

mask_green = np.zeros((width, height), dtype=np.uint8)
mask_green[1::2, 1::2] = 1

kernel_green = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) / 3
after_mask_green = cv2.bitwise_and(g, g, mask=mask_green)
filtered_green = cv2.filter2D(after_mask_green, -1, kernel_green)

mask_red = np.zeros((width, height), dtype=np.uint8)
mask_red[:, 1::2] = 1
mask_red[1::2] = 0
mask_red[1::2, ::2] = 1

kernel_red = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) / 6
after_mask_red = cv2.bitwise_and(r, r, mask=mask_red)
filtered_red = cv2.filter2D(after_mask_red, -1, kernel_red)

part_one_image = cv2.merge((filtered_blue, filtered_green, filtered_red))

sqrt_blue = np.sqrt(np.square(after_mask_blue - filtered_blue))
sqrt_green = np.sqrt(np.square(after_mask_green - filtered_green))
sqrt_red = np.sqrt(np.square(after_mask_red - filtered_red))

difference_image = np.array(sqrt_blue + sqrt_green + sqrt_red).astype(np.uint8)

new_blue, new_green, new_red = cv2.split(part_one_image)

green_red = new_green - new_red
blue_red = new_blue - new_red

green_red = cv2.medianBlur(green_red, 1)
blue_red = cv2.medianBlur(blue_red, 1)

green_red = green_red + new_red
blue_red = blue_red + new_red

free_man = cv2.merge((blue_red, green_red, new_red))

do_images = np.concatenate((img, part_one_image), axis=1)
cv2.imshow("part one", do_images)
cv2.imshow("difference", difference_image)
cv2.imshow("freeman", free_man)
cv2.waitKey()
