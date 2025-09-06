import re

<<<<<<< HEAD
def redact_text(file):
=======
def redact_text(file, sensitivity_level):
    """
    Redact sensitive information from a text file based on sensitivity level.
    """
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
    # Read the file content
    text = file.read().decode('utf-8')
    print("Original Text (before redaction):", text)  # Debug statement

    # Apply redaction
<<<<<<< HEAD
    redacted_text = apply_direct_redaction(text)
=======
    redacted_text = apply_direct_redaction(text, sensitivity_level)
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
    print("Redacted Text (after redaction):", redacted_text)  # Debug statement

    return redacted_text

<<<<<<< HEAD
def apply_direct_redaction(text):
    # Define patterns for all levels
    patterns = {
        r'(?i)(password:?\s*)(.*)': '[REDACTED]',
        r'(?i)(api\s?key:?\s*)(.*)': '[REDACTED]',
        r'(?i)(secret\s?key:?\s*)(.*)': '[REDACTED]',
=======
def apply_direct_redaction(text, sensitivity_level):
    """
    Apply redaction patterns based on sensitivity level.
    """
    # Define patterns for each sensitivity level
    level_1_patterns = {
        r'(?i)(password:?\s*)(.*)': '[REDACTED]',
        r'(?i)(api\s?key:?\s*)(.*)': '[REDACTED]',
        r'(?i)(secret\s?key:?\s*)(.*)': '[REDACTED]',
    }

    level_2_patterns = {
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
        r'(?i)(name:?\s*)(.*)': '[REDACTED]',
        r'(?i)(address:?\s*)(.*)': '[REDACTED]',
        r'(?i)(registration\s?(no|number):?\s*)(.*)': '[REDACTED]',
        r'(?i)(phone\s?number:?\s*)(.*)': '[REDACTED]',
        r'(?i)(email:?\s*)(.*)': '[REDACTED]',
<<<<<<< HEAD
=======
    }

    level_3_patterns = {
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
        r'(?i)(aadhar\s?(card)?\s?number:?\s*)(.*)': '[REDACTED]',
        r'(?i)(pan\s?(card)?\s?number:?\s*)(.*)': '[REDACTED]',
        r'(?i)(vehicle\s?(no|number):?\s*)(.*)': '[REDACTED]',
        r'(?i)(credit\s?card\s?number:?\s*)(.*)': '[REDACTED]',
    }
<<<<<<< HEAD
    for pattern, replacement in patterns.items():
        text = re.sub(pattern, replacement, text)
=======

    all_patterns = {
        1: level_1_patterns,
        2: level_2_patterns,
        3: level_3_patterns,
    }

    # Apply patterns based on sensitivity level
    for level in range(1, sensitivity_level + 1):
        patterns = all_patterns.get(level, {})
        for pattern, replacement in patterns.items():
            text = re.sub(pattern, replacement, text)

>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
    return text