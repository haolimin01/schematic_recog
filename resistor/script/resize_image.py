import cv2
import os
P_IMAGE_SIZE = 20
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
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        except Exception:
            print(content, 'resizes failed!')
        img = cv2.resize(img, dsize=(P_IMAGE_SIZE, P_IMAGE_SIZE))
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
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        except Exception:
            print(content, ' resizes failed!')
        img = cv2.resize(img, dsize=(N_IMAGE_SIZE, N_IMAGE_SIZE))
        cv2.imwrite(content.strip('\n'), img=img)


if __name__ == '__main__':
    positive_resize()
    negative_resize()
