import cv2
import numpy as np


def main():
    img = cv2.imread("images/oldwell_mosaic.bmp")
    org = cv2.imread("images/oldwell.jpg")
    b, g, r = cv2.split(img)
    b_o, g_o, r_o = cv2.split(org)
    shape = get_shape(img)
    b_org, blue = prepare_channel(0, b, shape)
    g_org, green = prepare_channel(1, g, shape)
    r_org, red = prepare_channel(2, r, shape)

    final_img = cv2.merge((blue, green, red))
    squared_img = display_squared_values(b_o, g_o, r_o, blue, green, red)
    freeman_img = bill_freeman(blue, green, red)

    numpy_horizontal_concat = np.concatenate((img, final_img), axis=1)
    cv2.imshow("masked", numpy_horizontal_concat)
    cv2.imshow("root squared", squared_img)
    cv2.imshow("freeman", freeman_img)
    cv2.waitKey()


def bill_freeman(blue, green, red):
    g_r = green - red
    b_r = blue - red

    g_r = cv2.medianBlur(g_r, 1)
    b_r = cv2.medianBlur(b_r, 1)

    g_r = g_r + red
    b_r = b_r + red

    final_img = cv2.merge((b_r, g_r, red))
    return final_img


def display_squared_values(b_org, g_org, r_org, blue, green, red):
    b_sq = calculate_squared(b_org, blue)
    g_sq = calculate_squared(g_org, green)
    r_sq = calculate_squared(r_org, red)

    square_image = np.array(b_sq + g_sq + r_sq).astype(np.uint8)
    return square_image


def calculate_squared(org, out):
    return np.sqrt(np.square(org) - np.square(out))


def get_shape(img):
    height = img.shape[1]
    width = img.shape[0]

    return width, height


def calculate_difference(a, b):
    return a - b


# see the filter document to know the right one
def get_kernel():
    b_kernel = np.ones((5, 5), np.uint8) / 6
    g_kernel = np.ones((5, 5), np.uint8) / 6
    r_kernel = np.ones((5, 5), np.uint8) / 12

    return b_kernel, g_kernel, r_kernel


def fetch_mask(shape):
    b_mask = np.zeros(shape, dtype=np.uint8)
    b_mask[:, ::2] = 1
    b_mask[1::2] = 0

    g_mask = np.zeros(shape, dtype=np.uint8)
    g_mask[1::2, 1::2] = 1

    r_mask = np.zeros(shape, dtype=np.uint8)
    r_mask[:, 1::2] = 1
    r_mask[1::2] = 0
    r_mask[1::2, ::2] = 1

    return b_mask, g_mask, r_mask


def prepare_channel(channel_index, channel_matrix, shape):
    channel = cv2.bitwise_and(channel_matrix, channel_matrix, mask=fetch_mask(shape)[channel_index])
    filtered = cv2.filter2D(channel, -1, get_kernel()[channel_index])

    return channel, filtered


if __name__ == '__main__':
    main()
