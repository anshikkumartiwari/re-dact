<<<<<<< HEAD

```
srip
├─ 📁datasets
│  └─ 📁signature
│     ├─ 📁train
│     │  ├─ 📁images
│     │  ├─ 📁labels
│     ├─ 📁valid
│     │  ├─ 📁images
│     │  ├─ 📁labels
│     └─ 📄signature.yaml
├─ 📁services
│  ├─ 📁addons
│  │  ├─ 📄address.py
│  │  ├─ 📄best.pt
│  │  ├─ 📄digiSignBlur.py
│  │  ├─ 📄digiSignBlur2.py
│  │  ├─ 📄direct.py
│  │  ├─ 📄faceBlur.py
│  │  ├─ 📄nsfwBlur.py
│  │  ├─ 📄numPlateBlur.py
│  │  ├─ 📄numPlateDetecModel.pt
│  │  ├─ 📄ocrBlur.py
│  │  ├─ 📄patterns.py
│  │  └─ 📄removeMetadata.py
│  ├─ 📄docx.py
│  ├─ 📄img.py
│  ├─ 📄others.py
│  ├─ 📄pdf.py
│  ├─ 📄txt.py
│  └─ 📄__init__.py
├─ 📁static
│  ├─ 📁assets
│  ├─ 📁uploads
│  └─ 📄styles.css
├─ 📁templates
│  ├─ 📄index.html
│  └─ 📄result.html
├─ 📄app.py
├─ 📄tempCodeRunnerFile.py
└─ 📄yolov8n.pt
```


```
Title: Integrated Multimodal Redaction Architecture with Reversible Cryptographic Obfuscation

Design a formal flowchart for a research paper. Use a clean, modern layout with minimalistic icons or rectangular blocks. Arrange the flow vertically from top (input) to bottom (final output). Use labeled arrows to show data flow between modules.

Flowchart Structure:

1. Input Stage:
   - Label: DOCX File (Input)
   - Icon Suggestion: DOCX file or upload icon

2. Preprocessing Stage:
   - Box: docx.py
   - Two parallel arrows from docx.py:
     a. Text Elements → txt.py
     b. Image Elements → img.py

3. Text Redaction Subsystem:
   - Main Box: txt.py
   - Connects to smaller modules:
     • address.py
     • direct.py
     • patterns.py
   - Label this cluster as: "Sensitive Pattern Recognition"

4. Image Redaction Subsystem:
   - Main Box: img.py
   - Connects to submodules under "services/addons/":
     • faceBlur.py
     • ocrBlur.py
     • digiSignBlur.py
     • nsfwBlur.py
     • numPlateBlur.py
     • etc.
   - Indicate: "Redaction Info" returns to img.py
   - img.py applies: Reversible Obfuscation

5. Reconstruction Stage:
   - Output from txt.py and img.py return to docx.py
   - Final box: Reconstructed Redacted DOCX File (Output)

Visual Style Suggestions:
- Use color-coding: 
  • Blue for text flow
  • Green for image flow
- Smooth directional arrows
- Formal font and clear spacing
- Title the diagram at the top
```
=======
# RE-Dact Tool

<p>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Python-logo.png/219px-Python-logo.png" height="60">
  <img src="https://logowik.com/content/uploads/images/flask3998.jpg" height="60">
</p>


### Multi-file Format Automatic Redaction Tool

This is a Flask-based web application designed to automatically detect redact sensitive content from various file formats (.TXT, .JPG, .JPEG, .PNG, .DOCX, .ODT, etc.) without any dependency on external APIs or internet.

### Features

- Detects and blurs faces in images.
- Redacts vehicle license plates.
- Removes metadata from all files.
- Redacts signatures in images and documents.

---

## Example Frontend

![Frontend](Screenshot1.png)
![Frontend](Screenshot2.jpeg)

## Redaction in Action

![Demo image](redact_facecarsig.png)
Besides this, text contents, image metadata, OCR recognbised text content, nsfw content (build for this one is yet in progress) is also redacted.

---

## Project Directory Structure

bash 
```
re-dact/
├── __pycache__/
├── datasets/
│   └── signature/
│       ├── train/
│       ├── valid/
│       └── signature.yaml
├── services/
│   ├── __pycache__/
│   ├── addons/
│   │   ├── best.pt
│   │   ├── digiSignBlur.py
│   │   ├── digiSignBlur2.py
│   │   ├── direct.py
│   │   ├── faceBlur.py
│   │   ├── numPlateBlur.py
│   │   ├── numPlateDetecModel.pt
│   │   ├── ocrBlur.py
│   │   ├── patterns.py
│   │   ├── removeMetadata.py
│   │   └── placeholder.py
│   │   └── nsfwBlur.py
│   ├── __init__.py
│   ├── docx.py
│   ├── img.py
│   ├── others.py
│   ├── pdf.py
│   └── txt.py
├── static/
│   ├── assets/
│   │   ├── logo (1).png
│   │   ├── logo.png
│   │   ├── pattern.png
│   │   ├── pattern2.png
│   │   ├── vit.png
│   │   └── vit3.png
│   ├── uploads/
│   └── styles.css
├── templates/
├── app.py
├── pandoc-3.3-windows-x86_64.msi
└── tempCodeRunnerFile.py
```

## Installation

Make sure you have [Python 3.8+](https://www.python.org/) installed.

1. Clone the repository:

bash
git clone https://github.com/your-username/re-dact-tool.git
cd re-dact-tool


2. Install dependencies:

bash
pip install -r requirements.txt (will be available soon)


3. Run the application:

bash
python app.py


The app will be available at http://127.0.0.1:5000 in your browser.

You can use the following doxcx file to test all the attributes at once: https://docs.google.com/document/d/1lF5QyNvzsJLfRNGYXkuFtroFSQqbw68gWlmLpK550zA/pub

---

## Resources and References

Make sure you have [Python 3.8+](https://www.python.org/) installed.



0. digiSignBlur2.py:
This is based on my custom trained model on my self labeled dataset https://github.com/anshikkumartiwari/siginature-detection-blur 

1. digiSignBlur2.py:
Two modules are assigned to handle signatures one of them is sourced from https://github.com/ahmetozlu/signature_extractor with slight modifications.

2. numPlateBlur.py:
This one is sourced from BLANK_ with slight modifications.



---
>>>>>>> 1d9e9dad04fbdda5373b0cc55ac7bbf063c66a89
