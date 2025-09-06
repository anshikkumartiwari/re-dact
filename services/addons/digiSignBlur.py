from ultralytics import YOLO

def detect_signatures(input_path, model_path=r"services\addons\best.pt", conf_threshold=0.75):
    """
    Detect signatures in the image and return their bounding box coordinates.
    """
    
    model = YOLO(model_path)
    
    
    results = model.predict(source=input_path, conf=conf_threshold)
    
    
    signature_boxes = []
    for result in results:
        if result.boxes is not None:
            boxes = result.boxes.xyxy.cpu().numpy()  
            signature_boxes.extend([(int(x1), int(y1), int(x2 - x1), int(y2 - y1)) for x1, y1, x2, y2 in boxes])
    
    
    return signature_boxes