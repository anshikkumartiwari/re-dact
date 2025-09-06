import os
import tempfile
import pypandoc
from .txt import redact_text  

<<<<<<< HEAD
def process_other_file(file, file_ext):
=======
def process_other_file(file, file_ext, sensitivity_level):
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
    """
    Handle less common file types like .odt, .html, .epub, .md, and .rtf.
    Convert them to plain text, redact the text, and save them in the same format.
    """
    if file_ext == '.odt':
<<<<<<< HEAD
        return process_odt_file(file)
    elif file_ext == '.html':
        return process_html_file(file)
    elif file_ext == '.md':
        return process_md_file(file)
    elif file_ext == '.epub':
        return process_epub_file(file)
    elif file_ext == '.rtf':
        return process_rtf_file(file)
    else:
        raise ValueError(f"Unsupported file format: {file_ext}")

def process_odt_file(file):
=======
        return process_odt_file(file, sensitivity_level)
    elif file_ext == '.html':
        return process_html_file(file, sensitivity_level)
    elif file_ext == '.md':
        return process_md_file(file, sensitivity_level)
    elif file_ext == '.epub':
        return process_epub_file(file, sensitivity_level)
    elif file_ext == '.rtf':
        return process_rtf_file(file, sensitivity_level)
    else:
        raise ValueError(f"Unsupported file format: {file_ext}")

def process_odt_file(file, sensitivity_level):
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
    """
    Handle ODT files by saving them temporarily and converting via Pandoc.
    """
    
    temp_input_file = tempfile.NamedTemporaryFile(delete=False, suffix='.odt')
    file.save(temp_input_file.name)  

    
    text_content = pypandoc.convert_file(temp_input_file.name, 'plain', format='odt')
    
    
<<<<<<< HEAD
    redacted_text = redact_text(text_content.encode('utf-8'))
=======
    redacted_text = redact_text(text_content.encode('utf-8'), sensitivity_level)
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
    
    
    temp_output_file = tempfile.NamedTemporaryFile(delete=False, suffix='.odt')
    temp_output_file.write(redacted_text.encode('utf-8'))
    temp_output_file.close()

    
    os.unlink(temp_input_file.name)
    
    return temp_output_file.name

<<<<<<< HEAD
def process_html_file(file):
=======
def process_html_file(file, sensitivity_level):
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
    """
    Handle HTML files by saving them temporarily and converting via Pandoc.
    """
    temp_input_file = tempfile.NamedTemporaryFile(delete=False, suffix='.html')
    file.save(temp_input_file.name)  

    text_content = pypandoc.convert_file(temp_input_file.name, 'plain', format='html')
<<<<<<< HEAD
    redacted_text = redact_text(text_content.encode('utf-8'))
=======
    redacted_text = redact_text(text_content.encode('utf-8'), sensitivity_level)
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89

    temp_output_file = tempfile.NamedTemporaryFile(delete=False, suffix='.html')
    temp_output_file.write(redacted_text.encode('utf-8'))
    temp_output_file.close()

    os.unlink(temp_input_file.name)

    return temp_output_file.name

<<<<<<< HEAD
def process_md_file(file):
=======
def process_md_file(file, sensitivity_level):
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
    """
    Handle Markdown files by saving them temporarily and converting via Pandoc.
    """
    temp_input_file = tempfile.NamedTemporaryFile(delete=False, suffix='.md')
    file.save(temp_input_file.name)

    text_content = pypandoc.convert_file(temp_input_file.name, 'plain', format='md')
<<<<<<< HEAD
    redacted_text = redact_text(text_content.encode('utf-8'))
=======
    redacted_text = redact_text(text_content.encode('utf-8'), sensitivity_level)
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89

    temp_output_file = tempfile.NamedTemporaryFile(delete=False, suffix='.md')
    temp_output_file.write(redacted_text.encode('utf-8'))
    temp_output_file.close()

    os.unlink(temp_input_file.name)

    return temp_output_file.name

<<<<<<< HEAD
def process_epub_file(file):
=======
def process_epub_file(file, sensitivity_level):
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
    """
    Handle EPUB files by saving them temporarily and converting via Pandoc.
    """
    temp_input_file = tempfile.NamedTemporaryFile(delete=False, suffix='.epub')
    file.save(temp_input_file.name)

    text_content = pypandoc.convert_file(temp_input_file.name, 'plain', format='epub')
<<<<<<< HEAD
    redacted_text = redact_text(text_content.encode('utf-8'))
=======
    redacted_text = redact_text(text_content.encode('utf-8'), sensitivity_level)
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89

    temp_output_file = tempfile.NamedTemporaryFile(delete=False, suffix='.epub')
    temp_output_file.write(redacted_text.encode('utf-8'))
    temp_output_file.close()

    os.unlink(temp_input_file.name)

    return temp_output_file.name

<<<<<<< HEAD
def process_rtf_file(file):
=======
def process_rtf_file(file, sensitivity_level):
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
    """
    Handle RTF files by saving them temporarily and converting via Pandoc.
    """
    temp_input_file = tempfile.NamedTemporaryFile(delete=False, suffix='.rtf')
    file.save(temp_input_file.name)

    text_content = pypandoc.convert_file(temp_input_file.name, 'plain', format='rtf')
<<<<<<< HEAD
    redacted_text = redact_text(text_content.encode('utf-8'))
=======
    redacted_text = redact_text(text_content.encode('utf-8'), sensitivity_level)
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89

    temp_output_file = tempfile.NamedTemporaryFile(delete=False, suffix='.rtf')
    temp_output_file.write(redacted_text.encode('utf-8'))
    temp_output_file.close()

    os.unlink(temp_input_file.name)

    return temp_output_file.name