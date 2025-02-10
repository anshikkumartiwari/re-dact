from docx import Document
from services.img import process_image
import os
import tempfile
from services.addons.direct import apply_direct_redaction  # Import the redaction function


def extract_and_replace_images(doc, upload_folder, redact_ocr, redact_meta, redact_face, redact_license_plate, redact_signature, redact_nsfw, is_document, sensitivity_level):
    """
    Extract images from the docx file, process them, and replace them in the document.
    """
    image_replacements = {}
    
    # Loop through all relationships in the document to find images
    for rel in doc.part.rels.values():
        if "image" in rel.target_ref:
            image_data = rel.target_part.blob
            image_filename = os.path.join(upload_folder, os.path.basename(rel.target_ref))
            
            # Save the original image temporarily
            with open(image_filename, "wb") as f:
                f.write(image_data)
            
            # Process the image using img.py
            processed_image = process_image(image_filename, redact_ocr, redact_meta, redact_face, redact_license_plate, redact_signature, redact_nsfw, is_document, sensitivity_level)
            
            # Store the processed image for later replacement in the document
            with open(processed_image, "rb") as img_file:
                image_replacements[rel.target_ref] = img_file.read()
    
    # Replace original images with processed images in the document
    for rel in doc.part.rels.values():
        if rel.target_ref in image_replacements:
            rel.target_part._blob = image_replacements[rel.target_ref]
    
    return doc


def process_text_elements(element, sensitivity_level):
    """
    Recursively process all text elements (paragraphs, runs, tables, etc.) and apply redaction.
    """
    if hasattr(element, 'text') and element.text is not None:
        # Redact text in the element if it exists
        element.text = apply_direct_redaction(element.text, sensitivity_level)
    
    if hasattr(element, '_element'):
        # Process child elements recursively
        for child in element._element:
            process_text_elements(child, sensitivity_level)


def process_docx_file(docx_file, sensitivity_level, redact_ocr, redact_meta, redact_face, redact_license_plate, redact_signature, redact_nsfw, is_document):
    """
    Process a docx file by redacting text and replacing processed images.
    Create a new redacted .docx file while preserving the structure.
    """
    # Open the .docx file for reading
    doc = Document(docx_file)
    upload_folder = 'static/uploads'
    
    # Process all text elements (paragraphs, tables, headers, footers, etc.)
    for paragraph in doc.paragraphs:
        process_text_elements(paragraph, sensitivity_level)
    
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    process_text_elements(paragraph, sensitivity_level)
    
    # Step to extract, process, and replace images in the document
    doc = extract_and_replace_images(doc, upload_folder, redact_ocr, redact_meta, redact_face, redact_license_plate, redact_signature, redact_nsfw, is_document, sensitivity_level)
    
    # Save the redacted document to a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
    doc.save(temp_file.name)
    return temp_file.name