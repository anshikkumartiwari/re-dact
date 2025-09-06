import re

<<<<<<< HEAD
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




=======
# Phone number: Matches 10-digit phone numbers in India (e.g., 9876543210)
def redact_phone_numbers(text):
    return re.sub(r'\b\d{10}\b', '[REDACTED]', text)

# Aadhaar card: Matches both spaced and non-spaced 12-digit Aadhaar numbers
def redact_aadhaar_numbers(text):
    return re.sub(r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}\b', '[REDACTED]', text)

# PAN card: Matches Indian PAN card numbers (e.g., ABCDE1234F)
def redact_pan_numbers(text):
    return re.sub(r'\b[A-Z]{5}[0-9]{4}[A-Z]\b', '[REDACTED]', text)

# Vehicle number: Matches Indian vehicle numbers (e.g., UP14AC1417 or UP 14 AC 1417)
def redact_vehicle_numbers(text):
    return re.sub(r'\b[A-Z]{2}[ ]?\d{2}[ ]?[A-Z]{1,2}[ ]?\d{4}\b', '[REDACTED]', text)

# Credit Card Number: Matches 13 to 19-digit credit card numbers, with optional spaces or dashes
def redact_credit_card_numbers(text):
    return re.sub(r'\b(?:\d[ -]*){13,19}\b', '[REDACTED]', text)

# Passport Number: Matches Indian passport numbers (e.g., A1234567)
def redact_passport_numbers(text):
    return re.sub(r'\b[A-Z]{1}[0-9]{7}\b', '[REDACTED]', text)

# Voter ID: Matches Indian voter ID format (e.g., ABC1234567)
def redact_voter_id_numbers(text):
    return re.sub(r'\b[A-Z]{3}[0-9]{7}\b', '[REDACTED]', text)

# Bank Account Number: Matches 9 to 18-digit bank account numbers
def redact_bank_account_numbers(text):
    return re.sub(r'\b\d{9,18}\b', '[REDACTED]', text)

# IFSC Code: Matches Indian IFSC codes (e.g., SBIN0001234)
def redact_ifsc_codes(text):
    return re.sub(r'\b[A-Z]{4}0[A-Z0-9]{6}\b', '[REDACTED]', text)

# UPI ID: Matches standard UPI IDs (e.g., example@upi or user123@okhdfcbank)
def redact_upi_ids(text):
    return re.sub(r'\b[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\b', '[REDACTED]', text)

# Email Addresses: Matches most common email formats
def redact_email_addresses(text):
    return re.sub(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', '[REDACTED]', text)

# Combine all patterns into one function
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
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
<<<<<<< HEAD
    return text

=======
    return text
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
