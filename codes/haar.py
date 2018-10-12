import cv2
import os
P_IMAGE_SIZE = 32
N_IMAGE_SIZE = 256


def positive_resize():
    positive_label = '../data/positive/label'
    ret = os.path.exists(positive_label)
    if not ret:
        print('label not exists')
        exit
    contents = open(positive_label, 'r')
    for content in contents:
        img = cv2.imread(content.strip('\n'))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, dsize=(P_IMAGE_SIZE, P_IMAGE_SIZE))
        cv2.imwrite(content.strip('\n'), img=img)


def negative_resize():
    negative_label = '../data/negative/label'
    ret = os.path.exists(negative_label)
    if not ret:
        print('label not exists')
        exit
    contents = open(negative_label, 'r')
    for content in contents:
        img = cv2.imread(content.strip('\n'))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, dsize=(N_IMAGE_SIZE, N_IMAGE_SIZE))
        cv2.imwrite(content.strip('\n'), img=img)


def png_to_jpg():
    image_path = '../data/positive/p_0009.PNG'
    img = cv2.imread(image_path)
    new_name = image_path.replace('.PNG', '.JPEG')
    print(new_name)
    cv2.imwrite(new_name, img=img)


def classify():
    mos_haar = cv2.CascadeClassifier('/home/haolimin/Pycharm/data/xml/cascade.xml')
    test_image_path = '../data/test/0.JPG'
    image = cv2.imread(test_image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mos = mos_haar.detectMultiScale(gray_image)
    if len(mos) != 0:
        print('found')
        for x, y, w, h in mos:
            cv2.rectangle(gray_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imwrite('classify.JPG', gray_image)


if __name__ == '__main__':
    # png_to_jpg()
    # classify()
    positive_resize()



