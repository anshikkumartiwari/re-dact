import re

def redact_phone_numbers(text):
    return re.sub(r'\b\d{10}\b', '[REDACTED]', text)

def redact_aadhaar_numbers(text):
    return re.sub(r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}\b', '[REDACTED]', text)

def redact_pan_numbers(text):
    return re.sub(r'\b[A-Z]{5}[0-9]{4}[A-Z]\b', '[REDACTED]', text)

def redact_vehicle_numbers(text):
    return re.sub(r'\b[A-Z]{2}[ ]?\d{2}[ ]?[A-Z]{1,2}[ ]?\d{4}\b', '[REDACTED]', text)

def redact_credit_card_numbers(text):
    return re.sub(r'\b(?:\d[ -]*){13,19}\b', '[REDACTED]', text)

def redact_passport_numbers(text):
    return re.sub(r'\b[A-Z]{1}[0-9]{7}\b', '[REDACTED]', text)

def redact_voter_id_numbers(text):
    return re.sub(r'\b[A-Z]{3}[0-9]{7}\b', '[REDACTED]', text)

def redact_bank_account_numbers(text):
    return re.sub(r'\b\d{9,18}\b', '[REDACTED]', text)

def redact_ifsc_codes(text):
    return re.sub(r'\b[A-Z]{4}0[A-Z0-9]{6}\b', '[REDACTED]', text)

def redact_upi_ids(text):
    return re.sub(r'\b[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\b', '[REDACTED]', text)

def redact_email_addresses(text):
    return re.sub(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', '[REDACTED]', text)


def redact_aadhaar_numbers(text):
    # Accepts 12 digits with 0–2 spaces/dashes between groups
    return re.sub(r'\b\d{4}[\s\-]{0,2}\d{4}[\s\-]{0,2}\d{4}\b', '[REDACTED]', text)

def redact_credit_card_numbers(text):
    # Accepts 13–19 digits, with optional spaces or dashes
    return re.sub(r'\b(?:\d[\s\-]*){13,19}\b', '[REDACTED]', text)

def redact_ifsc_codes(text):
    # Allows small OCR mistakes: multiple spaces or 0 between
    return re.sub(r'\b[A-Z]{4}[\s]*0[\s]*[A-Z0-9]{6}\b', '[REDACTED]', text)

def redact_pan_numbers(text):
    return re.sub(r'\b[A-Z]{5}[0-9]{4}[A-Z]\b', '[REDACTED]', text)




def redact_patterns(text):
    text = redact_phone_numbers(text)
    text = redact_aadhaar_numbers(text)
    text = redact_pan_numbers(text)
    text = redact_vehicle_numbers(text)
    text = redact_credit_card_numbers(text)
    text = redact_passport_numbers(text)
    text = redact_voter_id_numbers(text)
    text = redact_bank_account_numbers(text)
    text = redact_ifsc_codes(text)
    text = redact_upi_ids(text)
    text = redact_email_addresses(text)
    return text

