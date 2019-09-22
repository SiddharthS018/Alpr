import io
import os
from google.cloud import vision_v1p3beta1 as vision
import cv2

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_key.json'

SOURCE_PATH = "E:\\TcS\HumaIn\\alpr\\recognize-license-plate\\"

def recognize_license_plate(img_path):

    img = cv2.imread(img_path)

    height, width = img.shape[:2]

    img = cv2.resize(img, (800, int((height * 800) / width)))

    cv2.imwrite(SOURCE_PATH + "output.jpg", img)

    img_path = SOURCE_PATH + "output.jpg"

    client = vision.ImageAnnotatorClient()

    with io.open(img_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    for text in texts:
        if len(text.description) == 10:
            license_plate = text.description
            print(license_plate)
         
path = SOURCE_PATH + '14.jpg'
recognize_license_plate(path)

