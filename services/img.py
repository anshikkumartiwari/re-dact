import os
import cv2
import numpy as np
from PIL import Image
import hashlib
import random
from services.addons.faceBlur import detect_faces
from services.addons.digiSignBlur import detect_signatures
from services.addons.digiSignBlur2 import detect_signatures_doc
from services.addons.numPlateBlur import detect_license_plates
from services.addons.removeMetadata import remove_metadata
from services.addons.ocrBlur import detect_text_with_ocr

# Hardcoded secret key for encryption/decryption
secret_key = "mysecretkey"

# keyblurimg_tile.py

from PIL import Image
import numpy as np
import hashlib
import random


from decimal import Decimal, getcontext

# Increase precision globally for the logistic map
getcontext().prec = 60

# fixed tile size for tolerance
_TILE_SIZE = 16

def logistic_map(seed, r=3.99, size=1):
    x = (seed % 10000) / 10000.0
    result = []
    for _ in range(size):
        x = r * x * (1 - x)
        result.append(int(x * 256) % 256)
    return result

# fixed tile size for tolerance
_TILE_SIZE = 16

def encrypt_region(image_path, x, y, w, h, key, output_path):
    image = Image.open(image_path).convert('RGB')
    np_img = np.array(image)
    H, W = np_img.shape[:2]

    # determine tile index range
    tx0 = max(0, x   // _TILE_SIZE)
    ty0 = max(0, y   // _TILE_SIZE)
    tx1 = min((W-1)//_TILE_SIZE, (x + w - 1)//_TILE_SIZE)
    ty1 = min((H-1)//_TILE_SIZE, (y + h - 1)//_TILE_SIZE)

    for ti in range(tx0, tx1 + 1):
        for tj in range(ty0, ty1 + 1):
            xs = ti * _TILE_SIZE
            ys = tj * _TILE_SIZE
            xe = min(xs + _TILE_SIZE, W)
            ye = min(ys + _TILE_SIZE, H)

            tile = np_img[ys:ye, xs:xe].copy()

            # derive per-tile seed
            hsh = hashlib.sha256(f"{key}{ti}{tj}".encode()).hexdigest()
            seed = int(hsh, 16) % (2**32)
            random.seed(seed)

            # XOR each pixel in the tile
            for i in range(tile.shape[0]):
                for j in range(tile.shape[1]):
                    r, g, b = tile[i, j]
                    tile[i, j] = [
                        r ^ random.randint(0, 255),
                        g ^ random.randint(0, 255),
                        b ^ random.randint(0, 255)
                    ]

            np_img[ys:ye, xs:xe] = tile

    result = Image.fromarray(np_img)
    result.save(output_path)
    return output_path


def decrypt_region(image_path, x, y, w, h, key, output_path):
    return encrypt_region(image_path, x, y, w, h, key, output_path) 

def process_image(file_path, redact_ocr, redact_meta, redact_face, redact_license_plate, redact_signature, redact_nsfw, is_document):
    import json
    
    if redact_meta:
        no_metadata_path = os.path.splitext(file_path)[0] + '_no_metadata' + os.path.splitext(file_path)[1]
        remove_metadata(file_path, no_metadata_path)
    else:
        no_metadata_path = file_path  
    image = cv2.imread(no_metadata_path)
    blur_regions = []
    region_info = []
    if redact_face:
        face_boxes = detect_faces(no_metadata_path)
        blur_regions.extend(face_boxes)
        for (x, y, w, h) in face_boxes:
            region_info.append({
                "category": "face",
                "region": {"x": int(x), "y": int(y), "width": int(w), "height": int(h)}
            })
    if redact_signature:
        if is_document:
            signature_boxes = detect_signatures_doc(no_metadata_path)
        else:
            signature_boxes = detect_signatures(no_metadata_path)
        blur_regions.extend(signature_boxes)
        for (x, y, w, h) in signature_boxes:
            region_info.append({
                "category": "signature",
                "region": {"x": int(x), "y": int(y), "width": int(w), "height": int(h)}
            })
    if redact_license_plate and not is_document:
        license_plate_boxes = detect_license_plates(no_metadata_path)
        blur_regions.extend(license_plate_boxes)
        for (x, y, w, h) in license_plate_boxes:
            region_info.append({
                "category": "license_plate",
                "region": {"x": int(x), "y": int(y), "width": int(w), "height": int(h)}
            })
    if redact_ocr:
        text_boxes = detect_text_with_ocr(no_metadata_path)
        blur_regions.extend(text_boxes)
        for (x, y, w, h) in text_boxes:
            region_info.append({
                "category": "ocr_text",
                "region": {"x": int(x), "y": int(y), "width": int(w), "height": int(h)}
            })
    final_output_path = os.path.splitext(no_metadata_path)[0] + '_final_output' + os.path.splitext(no_metadata_path)[1]
    base, ext = os.path.splitext(final_output_path)
    if blur_regions:
        temp_path = no_metadata_path
        for idx, (x, y, w, h) in enumerate(blur_regions):
            out_path = final_output_path if idx == len(blur_regions) - 1 else f"{base}_enc_{idx}{ext}"
            encrypt_region(temp_path, x, y, w, h, secret_key, out_path)
            temp_path = out_path
    else:
        cv2.imwrite(final_output_path, image)
    
    # Create detection log JSON file for single image processing
    original_filename = os.path.basename(file_path)
    json_filename = os.path.splitext(original_filename)[0] + '.json'
    json_path = os.path.join('static', 'uploads', json_filename)
    
    # Create detection log with image reference
    detection_log = []
    for region in region_info:
        detection_log.append({
            "image": original_filename,
            "region": region["region"],
            "category": region["category"]
        })
    
    # Write detection log JSON file
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(json_path, 'w', encoding='utf-8') as jf:
        json.dump(detection_log, jf, indent=2)
    
    return final_output_path, region_info

def decrypt_image(image_path, json_path, secret_key):
    """
    Decrypts a redacted image using the provided JSON log and secret key.
    Returns the path to the decrypted image.
    """
    import json
    import tempfile
    
    # Load JSON log
    with open(json_path, 'r', encoding='utf-8') as jf:
        detection_log = json.load(jf)
    
    # If no regions to decrypt, return original image
    if not detection_log:
        return image_path
    
    # Start with the redacted image
    temp_path = image_path
    
    # Apply decryption for each region
    for idx, entry in enumerate(detection_log):
        region = entry['region']
        x = int(region['x'])
        y = int(region['y'])
        w = int(region['width'])
        h = int(region['height'])
        
        # Create output path for decrypted image
        if idx == len(detection_log) - 1:
            # Final decrypted image
            base_name = os.path.splitext(os.path.basename(image_path))[0]
            ext = os.path.splitext(image_path)[1]
            output_path = os.path.join('static', 'uploads', f"{base_name}_decrypted{ext}")
        else:
            # Intermediate decrypted image
            base_name = os.path.splitext(os.path.basename(image_path))[0]
            ext = os.path.splitext(image_path)[1]
            output_path = os.path.join('static', 'uploads', f"{base_name}_dec_{idx}{ext}")
        
        # Decrypt the region
        decrypt_region(temp_path, x, y, w, h, secret_key, output_path)
        temp_path = output_path
    
    return temp_path
