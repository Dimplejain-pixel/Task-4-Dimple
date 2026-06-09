import cv2
import pytesseract

# Change this path if Tesseract is installed elsewhere
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_path = "sample.png"

image = cv2.imread(image_path)

if image is None:
    print("Image not found!")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    print("=" * 50)
    print("AI TEXT RECOGNITION SYSTEM")
    print("=" * 50)

    print("\nRecognized Text:\n")
    print(text)

    print("\nText Recognition Completed Successfully!")