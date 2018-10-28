import cv2
import os
P_IMAGE_W = 20
P_IMAGE_H = 50
N_IMAGE_SIZE = 256


def png_to_jpg():
    image_path = ''
    img = cv2.imread(image_path)
    new_name = image_path.replace('.PNG', '.JPEG')
    cv2.imwrite(new_name, img=img)


def positive_resize():
    positive_label = '../positive/label'
    ret = os.path.exists(positive_label)
    if not ret:
        print('label not exists')
        exit
    contents = open(positive_label, 'r')
    for content in contents:
        img = cv2.imread(content.strip('\n'))
        try:
            # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = binarization(img)
        except Exception:
            print(content, 'resizes failed!')
        img = cv2.resize(img, dsize=(P_IMAGE_W, P_IMAGE_H))
        cv2.imwrite(content.strip('\n'), img=img)


def negative_resize():
    negative_label = '../negative/label'
    ret = os.path.exists(negative_label)
    if not ret:
        print('label not exists')
        exit
    contents = open(negative_label, 'r')
    for content in contents:
        img = cv2.imread(content.strip('\n'))
        try:
            # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = binarization(img)
        except Exception:
            print(content, ' resizes failed!')
        img = cv2.resize(img, dsize=(N_IMAGE_SIZE, N_IMAGE_SIZE))
        cv2.imwrite(content.strip('\n'), img=img)


def binarization(image):
    gauss = cv2.GaussianBlur(image, (3, 3), 0)
    gray_image = cv2.cvtColor(gauss, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray_image, 0, 255, cv2.THRESH_OTSU)
    return binary


if __name__ == '__main__':
    positive_resize()
    negative_resize()
