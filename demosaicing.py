import cv2
import numpy as np

img = cv2.imread("images/oldwell_mosaic.bmp")

b, g, r = cv2.split(img)

height = img.shape[1]
width = img.shape[0]

b_kernel = np.ones((5, 5), np.uint8) / 6
g_kernel = np.ones((5, 5), np.uint8) / 6
r_kernel = np.ones((5, 5), np.uint8) / 12

b_mask = np.zeros((width, height), dtype=np.uint8)
b_mask[:, ::2] = 1
b_mask[1::2] = 0

b_masked = cv2.bitwise_and(b, b, mask=b_mask)
b_filtered = cv2.filter2D(b_masked, -1, b_kernel)

g_mask = np.zeros((width, height), dtype=np.uint8)
g_mask[1::2, 1::2] = 1

g_masked = cv2.bitwise_and(g, g, mask=g_mask)
g_filtered = cv2.filter2D(g_masked, -1, g_kernel)

r_mask = np.zeros((width, height), dtype=np.uint8)
r_mask[:, 1::2] = 1
r_mask[1::2] = 0
r_mask[1::2, ::2] = 1

r_masked = cv2.bitwise_and(r, r, mask=r_mask)
r_filtered = cv2.filter2D(r_masked, -1, r_kernel)

final_img = cv2.merge((b_filtered, g_filtered, r_filtered))

squared_r = np.sqrt(np.square(r_masked - r_filtered))
squared_b = np.sqrt(np.square(b_masked - b_filtered))
squared_g = np.sqrt(np.square(g_masked - g_filtered))

square_image = np.array(squared_r + squared_b + squared_g).astype(np.uint8)

numpy_horizontal_concat = np.concatenate((img, final_img), axis=1)
cv2.imshow("masked", numpy_horizontal_concat)
cv2.imshow("root squared", square_image)
cv2.waitKey()
