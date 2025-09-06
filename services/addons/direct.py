import re
<<<<<<< HEAD
from services.addons.patterns import redact_patterns

# Direct label patterns (more conservative now)
patterns = {
    r'(?i)(password:?\s*)(.*)': r'\1[REDACTED]',
    r'(?i)(api\s?key:?\s*)(.*)': r'\1[REDACTED]',
    r'(?i)(secret\s?key:?\s*)(.*)': r'\1[REDACTED]',
    r'(?i)(phone\s?number:?\s*)(\d{10})': r'\1[REDACTED]',
    r'(?i)(email:?\s*)([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})': r'\1[REDACTED]',
    r'(?i)(aadhar\s?(card)?\s?number:?\s*)(\d{4}[\s-]?\d{4}[\s-]?\d{4})': r'\1[REDACTED]',
    r'(?i)(pan\s?(card)?\s?number:?\s*)([A-Z]{5}[0-9]{4}[A-Z])': r'\1[REDACTED]',
    r'(?i)(vehicle\s?(no|number):?\s*)([A-Z]{2}\d{2}[A-Z]{1,2}\d{4})': r'\1[REDACTED]',
    r'(?i)(credit\s?card\s?number:?\s*)([0-9 -]{13,19})': r'\1[REDACTED]',
    r'(?i)(ifsc\s?code:?\s*)([A-Z]{4}0[A-Z0-9]{6})': r'\1[REDACTED]',
}

def apply_direct_redaction(text):
    for pattern, replacement in patterns.items():
        text = re.sub(pattern, replacement, text)
    text = redact_patterns(text)
    return text
=======
from services.addons.patterns import redact_patterns  # Import the redaction functions from patterns.py
from services.addons.address import redact_addresses, extract_addresses  # Import the redaction functions and address extraction from address.py

level_1_patterns = {
    r'(?i)(password:?\s*)(.*)': '[REDACTED]',
    r'(?i)(api\s?key:?\s*)(.*)': '[REDACTED]',
    r'(?i)(secret\s?key:?\s*)(.*)': '[REDACTED]',
}

level_2_patterns = {
    r'(?i)(name:?\s*)(.*)': '[REDACTED]',
    r'(?i)(address:?\s*)(.*)': '[REDACTED]',
    r'(?i)(registration\s?(no|number):?\s*)(.*)': '[REDACTED]',
    r'(?i)(phone\s?number:?\s*)(.*)': '[REDACTED]',
    r'(?i)(email:?\s*)(.*)': '[REDACTED]',
}

level_3_patterns = {
    r'(?i)(aadhar\s?(card)?\s?number:?\s*)(.*)': '[REDACTED]',
    r'(?i)(pan\s?(card)?\s?number:?\s*)(.*)': '[REDACTED]',
    r'(?i)(vehicle\s?(no|number):?\s*)(.*)': '[REDACTED]',
    r'(?i)(credit\s?card\s?number:?\s*)(.*)': '[REDACTED]',
}

all_patterns = {
    1: level_1_patterns,
    2: level_2_patterns,
    3: level_3_patterns,
}

def apply_direct_redaction(text, sensitivity_level):
    # Apply direct redaction based on sensitivity level
    for level in range(1, sensitivity_level + 1):
        patterns = all_patterns.get(level, {})
        for pattern, replacement in patterns.items():
            text = re.sub(pattern, r'\1[REDACTED]', text)
    
    # Apply additional redaction using patterns from patterns.py
    text = redact_patterns(text)
    
    # Extract and redact addresses
    extracted_addresses = extract_addresses(text)
    text = redact_addresses(text, extracted_addresses)
    
    return text
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
