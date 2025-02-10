import cv2

def detect_faces(input_path):
    """
    Detect faces in the image and return their bounding box coordinates.
    """
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    image = cv2.imread(input_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7, minSize=(30, 30))
    
    
    return [(x, y, w, h) for (x, y, w, h) in faces]