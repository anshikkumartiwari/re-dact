import fitz  
import tempfile
import os
from services.txt import redact_text
from services.img import process_image

def process_pdf_file(file, sensitivity_level):
    """
    Process a PDF file: redact text, process images, and return the path to the redacted file.
    """
    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_input_file:
        file.save(temp_input_file.name)  

    doc = None  

    try:
        
        doc = fitz.Document(temp_input_file.name)  
        redacted_pdf = fitz.Document()  

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text("text")

            
            redacted_text = redact_text(text.encode('utf-8'), sensitivity_level).decode('utf-8')

            
            redacted_page = redacted_pdf.new_page(width=page.rect.width, height=page.rect.height)

            
            redacted_page.insert_text((72, 72), redacted_text, fontsize=12, color=(0, 0, 0))  

            
            image_list = page.get_images(full=True)
            for img_index, img in enumerate(image_list):
                xref = img[0]
                image_bytes = doc.extract_image(xref)["image"]

                
                with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_img_file:
                    temp_img_file.write(image_bytes)
                    temp_img_file.flush()  

                
                processed_img_path = process_image(temp_img_file.name)
                
                
                if not processed_img_path or not os.path.exists(processed_img_path):
                    raise RuntimeError(f"Processed image file is invalid or missing: {processed_img_path}")

                
                if os.path.getsize(processed_img_path) == 0:
                    raise RuntimeError(f"Processed image file is empty: {processed_img_path}")

                
                processed_img = fitz.Document(processed_img_path)
                image_rect = page.get_image_rects(xref)[0]  
                redacted_page.insert_image(image_rect, stream=processed_img.extract_image(0)["image"])

                
                processed_img.close()

        
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_output_file:
            redacted_pdf.save(temp_output_file.name)
            
            if os.path.getsize(temp_output_file.name) == 0:
                raise RuntimeError(f"Redacted PDF file is empty: {temp_output_file.name}")

        
        redacted_pdf.close()
        doc.close()  

        
        os.unlink(temp_input_file.name)

        return temp_output_file.name

    except Exception as e:
        
        if doc is not None and not doc.is_closed:
            doc.close()
        if os.path.exists(temp_input_file.name):
            os.unlink(temp_input_file.name)
        raise RuntimeError(f"Error processing PDF: {str(e)}")
