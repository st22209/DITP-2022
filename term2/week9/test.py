import cv2

img = cv2.imread("grey.jpeg", 0)

width, height = len(img), len(img[0])


def get_pixel_value(x: int, y: int) -> int | None:
    x -= 1
    y -= 1
    return img[x][y]


print(get_pixel_value(0, 0))
