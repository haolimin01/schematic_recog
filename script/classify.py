import cv2
import os


def classify(xml_path, image):
    if not os.path.exists(xml_path):
        print(xml_path, ' does not exist ...')
        return False, None
    feature = cv2.CascadeClassifier(xml_path)
    gauss = cv2.GaussianBlur(image, (3, 3), 0)
    gray_image = cv2.cvtColor(gauss, cv2.COLOR_BGR2GRAY)
    target = feature.detectMultiScale(gray_image)
    if len(target) != 0:
        return True, target
    else:
        return False, None


def load_image(path):
    image = cv2.imread(path)
    return image


def clear_pixel(image, x, y, w, h):
    width = image.shape[0]
    height = image.shape[1]
    if x > height or x + w > height or y > width or y + h > width:
        print('The parameters beyond the shape of image.')
        return False, None
    else:
        for i in range(y, y + h):
            for j in range(x, x + w):
                image[i][j] = 255
    return True, image


def binarization(image):
    gauss = cv2.GaussianBlur(image, (3, 3), 0)
    gray_image = cv2.cvtColor(gauss, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray_image, 0, 255, cv2.THRESH_OTSU)
    return binary


def classfy_all():
    image_path = '/home/haolimin/github/schematic_recog/test/2.jpg' #2.jpg无字母
    mos_xml = '/home/haolimin/github/schematic_recog/data/mos/xml/cascade.xml'
    ground_xml = '/home/haolimin/github/schematic_recog/data/ground/xml/cascade.xml'
    capacitor_xml = '/home/haolimin/github/schematic_recog/data/capacitor/xml/cascade.xml'
    source_xml = '/home/haolimin/github/schematic_recog/data/source/xml/cascade.xml'
    resistor_xml = '/home/haolimin/github/schematic_recog/data/resistor/xml/cascade.xml'
    xmls = [mos_xml, ground_xml, capacitor_xml, source_xml, resistor_xml]

    original_image = load_image(image_path)
    binary_image = binarization(original_image)
    for index, feature in enumerate(xmls):
        ret, feature = classify(xmls[index], original_image)
        if ret:
            for x, y, w, h in feature:
                clear_pixel(binary_image, x, y, w, h)
    cv2.imwrite('/home/haolimin/github/schematic_recog/test/result.jpg', binary_image)
    return binary_image


def main():
    classfy_all()


if __name__ == '__main__':
    main()
