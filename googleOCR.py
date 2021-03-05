import base64
import io
import os
import requests
import json
# Imports the Google Cloud client library
from google.cloud import vision

APIKEY = "AIzaSyDY9x5fQsP3bz0Q2WTXFcAc7cC6yRR00os"
GOOGLE_VISION_API_URL = "https://vision.googleapis.com/v1/images:annotate?key=" + APIKEY

# Instantiates a client
client = vision.ImageAnnotatorClient()


# The name of the image file to annotate
# file_name = "crop.jpg"

def googleOCRFunc(file_name):
    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        encoded_string = base64.urlsafe_b64encode(image_file.read())

    encoded_image = encoded_string.decode("utf-8")

    data2 = {
        "requests": [
            {
                "image": {
                    "content": encoded_image
                },
                "features": [
                    {
                        "type": "TEXT_DETECTION"
                    }
                ]
            }
        ]
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.post(url=GOOGLE_VISION_API_URL, json=data2)
    print(response.json())
    return response.json()


def googleOCRFunc2(file_name):
    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        encoded_string = base64.urlsafe_b64encode(image_file.read())

    encoded_image = encoded_string.decode("utf-8")

    data2 = {
        "requests": [
            {
                "image": {
                    "content": encoded_image
                },
                "features": [
                    {
                        "type": "DOCUMENT_TEXT_DETECTION"
                    }
                ]
            }
        ]
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.post(url=GOOGLE_VISION_API_URL, json=data2)
    print(response.json())
    return response.json()


# resultJSON = googleOCRFunc2("C:/Users/kench/PycharmProjects/pythonProject2/result/0_cropped_img.jpg")
#
# # resultJSON={'responses': [{'textAnnotations': [{'locale': 'zh', 'description': '尺\n击 立\n', 'boundingPoly': {'vertices': [{'x': 61, 'y': 32}, {'x': 252, 'y': 32}, {'x': 252, 'y': 66}, {'x': 61, 'y': 66}]}}, {'description': '尺', 'boundingPoly': {'vertices': [{'x': 61, 'y': 32}, {'x': 69, 'y': 32}, {'x': 69, 'y': 61}, {'x': 61, 'y': 61}]}}, {'description': '击', 'boundingPoly': {'vertices': [{'x': 88, 'y': 32}, {'x': 97, 'y': 32}, {'x': 97, 'y': 66}, {'x': 88, 'y': 66}]}}, {'description': '立', 'boundingPoly': {'vertices': [{'x': 243, 'y': 32}, {'x': 252, 'y': 32}, {'x': 252, 'y': 66}, {'x': 243, 'y': 66}]}}], 'fullTextAnnotation': {'pages': [{'property': {'detectedLanguages': [{'languageCode': 'zh', 'confidence': 0.67}]}, 'width': 315, 'height': 62, 'blocks': [{'boundingBox': {'vertices': [{'x': 61, 'y': 32}, {'x': 69, 'y': 32}, {'x': 69, 'y': 61}, {'x': 61, 'y': 61}]}, 'paragraphs': [{'boundingBox': {'vertices': [{'x': 61, 'y': 32}, {'x': 69, 'y': 32}, {'x': 69, 'y': 61}, {'x': 61, 'y': 61}]}, 'words': [{'boundingBox': {'vertices': [{'x': 61, 'y': 32}, {'x': 69, 'y': 32}, {'x': 69, 'y': 61}, {'x': 61, 'y': 61}]}, 'symbols': [{'property': {'detectedBreak': {'type': 'LINE_BREAK'}}, 'boundingBox': {'vertices': [{'x': 61, 'y': 32}, {'x': 69, 'y': 32}, {'x': 69, 'y': 61}, {'x': 61, 'y': 61}]}, 'text': '尺', 'confidence': 0.08}], 'confidence': 0.08}], 'confidence': 0.08}], 'blockType': 'TEXT', 'confidence': 0.08}, {'property': {'detectedLanguages': [{'languageCode': 'zh', 'confidence': 1}]}, 'boundingBox': {'vertices': [{'x': 88, 'y': 31}, {'x': 252, 'y': 32}, {'x': 252, 'y': 67}, {'x': 88, 'y': 66}]}, 'paragraphs': [{'property': {'detectedLanguages': [{'languageCode': 'zh', 'confidence': 1}]}, 'boundingBox': {'vertices': [{'x': 88, 'y': 31}, {'x': 252, 'y': 32}, {'x': 252, 'y': 67}, {'x': 88, 'y': 66}]}, 'words': [{'property': {'detectedLanguages': [{'languageCode': 'zh'}]}, 'boundingBox': {'vertices': [{'x': 88, 'y': 32}, {'x': 97, 'y': 32}, {'x': 97, 'y': 66}, {'x': 88, 'y': 66}]}, 'symbols': [{'property': {'detectedLanguages': [{'languageCode': 'zh'}], 'detectedBreak': {'type': 'SPACE'}}, 'boundingBox': {'vertices': [{'x': 88, 'y': 32}, {'x': 97, 'y': 32}, {'x': 97, 'y': 66}, {'x': 88, 'y': 66}]}, 'text': '击', 'confidence': 0.98}], 'confidence': 0.98}, {'property': {'detectedLanguages': [{'languageCode': 'zh'}]}, 'boundingBox': {'vertices': [{'x': 243, 'y': 32}, {'x': 252, 'y': 32}, {'x': 252, 'y': 66}, {'x': 243, 'y': 66}]}, 'symbols': [{'property': {'detectedLanguages': [{'languageCode': 'zh'}], 'detectedBreak': {'type': 'LINE_BREAK'}}, 'boundingBox': {'vertices': [{'x': 243, 'y': 32}, {'x': 252, 'y': 32}, {'x': 252, 'y': 66}, {'x': 243, 'y': 66}]}, 'text': '立', 'confidence': 0.71}], 'confidence': 0.71}], 'confidence': 0.84}], 'blockType': 'TEXT', 'confidence': 0.84}]}], 'text': '尺\n击 立\n'}}]}
#
# with open('OCRresult.json', 'w') as jsonfile:
#     json.dump(resultJSON, jsonfile)