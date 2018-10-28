import cv2
import numpy as np
import os


def rotation90():
    image_label = '../temp/label'
    ret = os.path.exists(image_label)
    if not ret:
        print('label not exists')
        exit
    contents = open(image_label, 'r')
    for content in contents:
        img = cv2.imread(content.strip('\n'))
        try:
            img = np.rot90(img)
        except Exception:
            print(content, 'rotation failed!')
        cv2.imwrite(content.strip('\n'), img=img)


if __name__ == '__main__':
    rotation90()
