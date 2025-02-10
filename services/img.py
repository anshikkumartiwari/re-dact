import os
import cv2
import numpy as np
from services.addons.faceBlur import detect_faces
from services.addons.digiSignBlur import detect_signatures
from services.addons.digiSignBlur2 import detect_signatures_doc
from services.addons.numPlateBlur import detect_license_plates
from services.addons.removeMetadata import remove_metadata
from services.addons.ocrBlur import detect_text_with_ocr

def apply_blur(image, boxes, blur_kernel_size=(99, 99)):
    """
    Apply Gaussian blur to multiple regions of an image based on bounding boxes.
    """
    for (x, y, w, h) in boxes:
        roi = image[y:y+h, x:x+w]
        blurred_roi = cv2.GaussianBlur(roi, blur_kernel_size, 30)
        image[y:y+h, x:x+w] = blurred_roi
    return image

from services.addons.ocrBlur import detect_text_with_ocr

def process_image(file_path, redact_ocr, redact_meta, redact_face, redact_license_plate, redact_signature, redact_nsfw, is_document, sensitivity_level):
    
    if redact_meta:
        no_metadata_path = os.path.splitext(file_path)[0] + '_no_metadata' + os.path.splitext(file_path)[1]
        remove_metadata(file_path, no_metadata_path)
    else:
        no_metadata_path = file_path  
    
    
    image = cv2.imread(no_metadata_path)
    
    
    blur_regions = []
    
    
    if redact_face:
        face_boxes = detect_faces(no_metadata_path)
        blur_regions.extend(face_boxes)
    
    
    if redact_signature:
        if is_document:
            signature_boxes = detect_signatures_doc(no_metadata_path)
        else:
            signature_boxes = detect_signatures(no_metadata_path)
        blur_regions.extend(signature_boxes)
    
    
    if redact_license_plate and not is_document:
        license_plate_boxes = detect_license_plates(no_metadata_path)
        blur_regions.extend(license_plate_boxes)
    
    
    if redact_ocr:
        text_boxes = detect_text_with_ocr(no_metadata_path)
        blur_regions.extend(text_boxes)
    
    
    if blur_regions:
        image = apply_blur(image, blur_regions)
    
    
    final_output_path = os.path.splitext(no_metadata_path)[0] + '_final_output' + os.path.splitext(no_metadata_path)[1]
    cv2.imwrite(final_output_path, image)
    
    return final_output_path