import re
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
