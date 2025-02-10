import cv2
import pytesseract
from pytesseract import Output
from services.addons.patterns import redact_patterns  # Import redaction module

def detect_text_with_ocr(image_path):
    """
    Detect text regions in an image using OCR and return their bounding box coordinates.
    
    Args:
        image_path (str): Path to the input image.
    
    Returns:
        list: List of bounding boxes [(x, y, w, h)] for detected text regions that need redaction.
    """
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image not found or unable to load: {image_path}")
    
    # Convert the image to RGB (Tesseract works better with RGB images)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Extract text using OCR
    d = pytesseract.image_to_data(image, output_type=Output.DICT, lang='eng')
    
    # Collect bounding boxes for text regions that need redaction
    redacted_boxes = []
    for i, word in enumerate(d['text']):
        if word.strip():  # Ignore empty words
            redacted_word = redact_patterns(word)  # Apply regex-based redaction
            
            # If redaction occurred (i.e., the word was modified), add its bounding box
            if redacted_word != word:
                x, y, w, h = d['left'][i], d['top'][i], d['width'][i], d['height'][i]
                redacted_boxes.append((x, y, w, h))
    
    # Return the list of bounding boxes for redaction
    return redacted_boxes