import spacy
import re


nlp = spacy.load("en_core_web_trf")

def extract_addresses(text):
    """
    Uses spaCy's transformer-based model to extract location-based entities.
    """
    doc = nlp(text)
    address_entities = [ent.text for ent in doc.ents if ent.label_ in ["GPE", "FAC", "LOC"]]
    return list(set(address_entities))  

def extract_address_components(text):
    """
    Uses regex to detect house numbers, street names, government quarters, and other address components.
    """
    patterns = [
        
        r"\b(?:Flat|House|Plot|Apt|Apartment|H\.No|Door|Building|Villa)\s?No\.?\s?\d+[A-Z]?\b",
        r"\b\d{1,3}/\d{1,3}\b",  
        r"\b(?:Sector|Block|Phase)\s?\d+\b",  
        r"\b(?:Tower|Wing|Floor|Unit)\s?[A-Z]?-?\d+\b",  

        
        r"\b(?:Street|St|Lane|Road|Avenue|Residency|Bypass|Ring\s?Road|Expressway|Circle)\s?\d*\b",
        r"\b(?:MG\s?Road|Ring\s?Road|Brigade\s?Road|Main\s?Street|Residency\s?Road|Indiranagar|Koramangala|Marathahalli|Sarjapur|Whitefield|HSR\s?Layout|Jayanagar|Banjara\s?Hills|Gachibowli|Connaught\s?Place|Rajajinagar)\b",

        
        r"\b\d{6}\b",

        
        r"\b(?:NH|SH|AH)\s?-?\d+\b",  
        r"\b(?:National\s?Highway|State\s?Highway)\s?\d+\b",

        
        r"\b(?:ME|HIG|MIG|LIG|EWS|TDI|CIDCO|BDA|DDA|ATS|DLF|MHADA)-?\d{1,4}[A-Z]?\b",

        
        r"\bQTR\s?No\.?\s?\d+\b",
        r"\bRailway Colony Quarter \d+[A-Z]?\b",
        r"\bP&T Colony House No\.?\s?\d+\b",
        r"\b(?:Type\s?[IVXLCDM]+|Govt\.?\s?Quarters|DRDO\s?Complex|Police\s?Colony)\s?No\.?\s?\d+\b",

        
        r"\bTower \d+, Apartment \d+[A-Z]?\b",
        r"\bBuilding \d+, Flat \d+[A-Z]?\b",
        r"\bBlock [A-Z], Villa \d+\b",
        r"\b(?:Prestige|Sobha|Brigade|Puravankara|Godrej|Embassy|ATS|DLF|Jaypee)\s?(?:Residency|Enclave|City|Green|Vistas|Palms|Heights|Oasis|Phase\s?\d+|County)\s?\d*\b",
        r"\b(?:Palm Meadows|Raheja Vihar|Salarpuria Sattva|Orchid Metropolis|Emaar Hills|Unitech Cyber Park|Hiranandani Gardens)\b",

        
        r"\b(?:Industrial\s?Estate|SEZ|Tech\s?Park|IT\s?Hub|Business\s?District|Electronic\s?City|Cyber\s?Park)\b",
        r"\b(?:DLF\s?Cyber\s?City|Manyata\s?Tech\s?Park|HITEC\s?City|Infocity|Mindspace|RMZ\s?Ecoworld)\b",

        
        r"\b(?:Near\s)?(?:Railway\s?Station|Metro\s?Station|Bus\s?Stand|Airport)\b",

        
        r"\b(?:Opposite|Near|Beside|Behind|Adjacent\s?to)\s?(?:Mall|Hotel|Theater|Temple|Church|Mosque|Stadium|Hospital|School|College|University|Landmark)\b"
    ]


    matches = set()
    for pattern in patterns:
        matches.update(re.findall(pattern, text, re.IGNORECASE))

    return list(matches)

def redact_addresses(text, addresses):
    """
    Replaces extracted addresses and components with '[REDACTED]'.
    """
    for address in sorted(addresses, key=len, reverse=True):  
        text = re.sub(r"\b" + re.escape(address) + r"\b", "[REDACTED]", text)
    return text