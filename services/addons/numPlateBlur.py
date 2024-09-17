import cv2
import numpy as np
import pytesseract
from ultralytics import YOLO


npDetecModel = YOLO(r'services\addons\numPlateDetecModel.pt')


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def has_large_text(license_plate_roi, text_threshold=20):
    """
    Function to check if the detected license plate has significant text using Tesseract OCR.
    """
    gray_roi = cv2.cvtColor(license_plate_roi, cv2.COLOR_BGR2GRAY)
    extracted_text = pytesseract.image_to_string(gray_roi, config='--psm 6')
    if len(extracted_text) > text_threshold:
        return True
    return False

def detect_and_blur_license_plate(image_path, output_path):
    """
    Function to detect and blur license plates in an image.
    """
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Image not found or unable to load: {image_path}")

    
    results = npDetecModel(img)

    for license_plate in results[0].boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = license_plate
        x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
        license_plate_roi = img[y1:y2, x1:x2]
        
        
        if has_large_text(license_plate_roi):
            continue

        
        blurred_roi = cv2.GaussianBlur(license_plate_roi, (23, 23), 30)
        img[y1:y2, x1:x2] = blurred_roi

    
    cv2.imwrite(output_path, img)
    print(f"Output saved to: {output_path}")
