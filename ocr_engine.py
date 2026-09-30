from PIL import Image
import pytesseract

# Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = (
    r"D:\Program Files\Tesseract-OCR\tesseract.exe"
)


def extract_text_from_image(image):
    try:
        text = pytesseract.image_to_string(image)
        return text.strip()

    except Exception as error:
        return f"OCR Error: {error}"


if __name__ == "__main__":
    image_path = "test_screenshot.png"

    image = Image.open(image_path)

    extracted_text = extract_text_from_image(image)

    print("--------------------------------")
    print("       OCR ENGINE")
    print("--------------------------------")
    print("Extracted Text:")
    print(extracted_text)