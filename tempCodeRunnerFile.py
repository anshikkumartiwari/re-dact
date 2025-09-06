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
        # Extract sensitivity level from the form
        sensitivity = int(request.form['sensitivity'])
        sensitivity_level = determine_sensitivity_level(sensitivity)

        # Handle text files separately
        if file_ext == '.txt':
            redacted_text = redact_text(file, sensitivity_level)
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.txt')
            temp_file.write(redacted_text.encode('utf-8'))
            temp_file.close()
            return render_template('result.html', redacted_text=redacted_text, file_path=temp_file.name, original_file=None)
        
        # Handle image and document files based on user-selected options
        elif file_ext in ['.png', '.jpg', '.jpeg', '.docx', '.pdf']:
            # Save the file to the uploads folder
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Get checkbox values from the form
            redact_ocr = 'redact_ocr' in request.form
            redact_meta = 'redact_meta' in request.form
            redact_face = 'redact_face' in request.form
            redact_license_plate = 'redact_license_plate' in request.form
            redact_signature = 'redact_signature' in request.form
            redact_nsfw = 'redact_nsfw' in request.form
            is_document = 'doc_check' in request.form

            # Process the image or document accordingly
            if file_ext in ['.png', '.jpg', '.jpeg']:
                final_image_path = process_image(file_path, redact_ocr, redact_meta, redact_face, redact_license_plate, redact_signature, redact_nsfw, is_document, sensitivity_level)
                final_image_name = os.path.basename(final_image_path)
                return render_template('result.html', original_file=file_path, image_name=final_image_name, image_path=final_image_path)

            elif file_ext == '.docx':
                redacted_docx_path = process_docx_file(file, sensitivity_level)
                return render_template('result.html', docx_file_path=redacted_docx_path, original_file=file_path)

            elif file_ext == '.pdf':
                redacted_pdf_path = process_pdf_file(file, sensitivity_level)
                return render_template('result.html', pdf_file_path=redacted_pdf_path, original_file=file_path)

        else:
            redacted_file_path = process_other_file(file, file_ext, sensitivity_level)
            return render_template('result.html', file_path=redacted_file_path, original_file=file_path)

    except Exception as e:
        return f"Error processing file: {str(e)}"


@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    """
    Allow users to download the processed file.
    """
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
