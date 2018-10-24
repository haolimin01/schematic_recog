import cv2
import os


def classify(xml_path, image):
    if not os.path.exists(xml_path):
        print(xml_path, ' does not exist ...')
        return False, None
    feature = cv2.CascadeClassifier(xml_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    target = feature.detectMultiScale(gray_image)
    if len(target) != 0:
        return True, target
    else:
        return False, None


def load_image(path):
    image = cv2.imread(path)
    return image


def main():
    origin_image = '/home/haolimin/adaboost+haar/data/test/2.jpg' #2.jpg无字母
    mos_xml = '/home/haolimin/adaboost+haar/data/train/mos/xml/cascade.xml'
    ground_xml = '/home/haolimin/adaboost+haar/data/train/ground/xml/cascade.xml'
    capacitor_xml = '/home/haolimin/adaboost+haar/data/train/capacitor/xml/cascade.xml'
    source_xml = '/home/haolimin/adaboost+haar/data/train/source/xml/cascade.xml'
    resistor_xml = '/home/haolimin/adaboost+haar/data/train/resistor/xml/cascade.xml'
    xmls = [mos_xml, ground_xml, capacitor_xml, source_xml, resistor_xml]

    show_image = load_image(origin_image)
    index = -1
    cv2.namedWindow('output', 0);
    cv2.resizeWindow('output', 960, 720);
    while True:
        if index >= 0:
            ret, feature = classify(xmls[index], show_image)
            if ret:
                for x, y, w, h in feature:
                    cv2.rectangle(show_image, (x, y), (x + w, y + h), (0, 0, 0), 2)
        cv2.imshow('output', show_image)
        k = cv2.waitKey(0) & 0xFF
        # m is pressed
        if k == 109:
            index = index + 1
            if index >= xmls.__len__():
                index = -1
                show_image = load_image(origin_image)
        # q is pressed
        elif k == 113:
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
