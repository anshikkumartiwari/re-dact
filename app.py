from flask import Flask, render_template, request, send_file, redirect, url_for
from services.txt import redact_text
from services.img import process_image
from services.docx import process_docx_file
from services.pdf import process_pdf_file
from services.others import process_other_file
import os
import tempfile
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

<<<<<<< HEAD
=======
def determine_sensitivity_level(slider_value):
    """
    Determine the sensitivity level based on the slider input value.
    """
    if 0 <= slider_value <= 33:
        return 1
    elif 34 <= slider_value <= 66:
        return 2
    elif 67 <= slider_value <= 100:
        return 3
    else:
        return 1  # Default to minimum sensitivity if out of bounds

>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
@app.route('/')
def index():
    """
    Render the index page where users can upload files.
    """
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handle file uploads, process text or image files, and return results based on checkboxes.
    """
    if 'file' not in request.files:
        return 'No file part in the request'
    
    file = request.files['file']
    if file.filename == '':
        return 'No file selected'

    filename = secure_filename(file.filename)
    file_ext = os.path.splitext(filename)[1].lower()

    try:
<<<<<<< HEAD
=======
        # Extract sensitivity level from the form
        sensitivity = int(request.form.get('sensitivity', 1))
        sensitivity_level = determine_sensitivity_level(sensitivity)

>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
        # Extract checkbox values from the form (ensure they are initialized properly)
        redact_ocr = 'redact_ocr' in request.form
        redact_meta = 'redact_meta' in request.form
        redact_face = 'redact_face' in request.form
        redact_license_plate = 'redact_license_plate' in request.form
        redact_signature = 'redact_signature' in request.form
        redact_nsfw = 'redact_nsfw' in request.form
        is_document = 'doc_check' in request.form

        # Save the uploaded file to the uploads folder
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(upload_path)  # Save file to static/uploads directory

        # Handle text files separately
        if file_ext == '.txt':
            # Read and pass the original text file content to the template
            with open(upload_path, 'r', encoding='utf-8') as f:
                original_text = f.read()

<<<<<<< HEAD
            redacted_text = redact_text(file)
=======
            redacted_text = redact_text(file, sensitivity_level)
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
            return render_template('result.html', redacted_text=redacted_text, original_text=original_text, file_path=upload_path, original_file=upload_path)
        
        # Handle image files
        elif file_ext in ['.png', '.jpg', '.jpeg']:
            # Process the image and generate the redacted version
<<<<<<< HEAD
            final_image_path, region_info = process_image(upload_path, redact_ocr, redact_meta, redact_face, redact_license_plate, redact_signature, redact_nsfw, is_document)
=======
            final_image_path = process_image(upload_path, redact_ocr, redact_meta, redact_face, redact_license_plate, redact_signature, redact_nsfw, is_document, sensitivity_level)
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
            final_image_name = os.path.basename(final_image_path)
            # Pass both the uploaded image and the processed image to the template
            return render_template('result.html', original_file=filename, image_name=final_image_name, image_path=final_image_path)

        # Handle DOCX files
        elif file_ext == '.docx':
            redacted_docx_path = process_docx_file(
<<<<<<< HEAD
                upload_path,  # pass the file path, not the FileStorage object
=======
                file, 
                sensitivity_level,
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
                redact_ocr,
                redact_meta,
                redact_face,
                redact_license_plate,
                redact_signature,
                redact_nsfw,
                is_document
            )
            return render_template('result.html', docx_file_path=redacted_docx_path, original_file=upload_path)

        # Handle PDF files
        elif file_ext == '.pdf':
<<<<<<< HEAD
            redacted_pdf_path = process_pdf_file(upload_path)
=======
            redacted_pdf_path = process_pdf_file(file, sensitivity_level)
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
            return render_template('result.html', pdf_file_path=redacted_pdf_path, original_file=upload_path)

        # Handle other files
        else:
<<<<<<< HEAD
            redacted_file_path = process_other_file(upload_path, file_ext)
=======
            redacted_file_path = process_other_file(file, file_ext, sensitivity_level)
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
            return render_template('result.html', file_path=redacted_file_path, original_file=upload_path)

    except Exception as e:
        return f"Error processing file: {str(e)}" 

@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    """
    Allow users to download the processed file.
    """
    file_path = os.path.join(app.root_path, filename)
    return send_file(file_path, as_attachment=True)

<<<<<<< HEAD
@app.route('/decrypt', methods=['POST'])
def decrypt_file():
    """
    Handle decryption of redacted DOCX using uploaded JSON and secret key.
    """
    docx_file = request.files.get('docx_file')
    json_file = request.files.get('json_file')
    secret_key = request.form.get('secret_key')

    if not docx_file or not json_file or not secret_key:
        return 'All fields are required.'

    # Save uploaded files
    upload_folder = app.config['UPLOAD_FOLDER']
    os.makedirs(upload_folder, exist_ok=True)
    docx_filename = secure_filename(docx_file.filename)
    json_filename = secure_filename(json_file.filename)
    docx_path = os.path.join(upload_folder, docx_filename)
    json_path = os.path.join(upload_folder, json_filename)
    docx_file.save(docx_path)
    json_file.save(json_path)

    # Call decryption logic in docx.py
    from services.docx import decrypt_docx_file
    decrypted_docx_path = decrypt_docx_file(docx_path, json_path, secret_key)

    return render_template('result.html', docx_file_path=decrypted_docx_path, original_file=docx_path)

=======
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
if __name__ == '__main__':
    app.run(debug=True)