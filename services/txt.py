import re

def redact_text(file):
    # Read the file content
    text = file.read().decode('utf-8')
    print("Original Text (before redaction):", text)  # Debug statement

    # Apply redaction
    redacted_text = apply_direct_redaction(text)
    print("Redacted Text (after redaction):", redacted_text)  # Debug statement

    return redacted_text

def apply_direct_redaction(text):
    # Define patterns for all levels
    patterns = {
        r'(?i)(password:?\s*)(.*)': '[REDACTED]',
        r'(?i)(api\s?key:?\s*)(.*)': '[REDACTED]',
        r'(?i)(secret\s?key:?\s*)(.*)': '[REDACTED]',
        r'(?i)(name:?\s*)(.*)': '[REDACTED]',
        r'(?i)(address:?\s*)(.*)': '[REDACTED]',
        r'(?i)(registration\s?(no|number):?\s*)(.*)': '[REDACTED]',
        r'(?i)(phone\s?number:?\s*)(.*)': '[REDACTED]',
        r'(?i)(email:?\s*)(.*)': '[REDACTED]',
        r'(?i)(aadhar\s?(card)?\s?number:?\s*)(.*)': '[REDACTED]',
        r'(?i)(pan\s?(card)?\s?number:?\s*)(.*)': '[REDACTED]',
        r'(?i)(vehicle\s?(no|number):?\s*)(.*)': '[REDACTED]',
        r'(?i)(credit\s?card\s?number:?\s*)(.*)': '[REDACTED]',
    }
    for pattern, replacement in patterns.items():
        text = re.sub(pattern, replacement, text)
    return text