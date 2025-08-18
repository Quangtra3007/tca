import cv2
import easyocr
import numpy as np
#Display image
def display(img, frameName="OpenCV Image"):
    h, w = img.shape[0:2]
    neww = 800
    newh = int(neww*(h/w))
    img = cv2.resize(img, (neww, newh))
    cv2.imshow(frameName, img)
    cv2.waitKey(0)

def detect_orientation(img):
    reader = easyocr.Reader(['en'])  # có thể thêm 'vi' nếu cần tiếng Việt

    # thử các góc: 0, 90, 180, 270
    best_angle = 0
    best_score = -1
    best_text = ""

    for angle in [0, 90, 180, 270]:
        # xoay ảnh
        if angle != 0:
            (h, w) = img.shape[:2]
            center = (w // 2, h // 2)
            M = cv2.getRotationMatrix2D(center, angle, 1.0)
            rotated = cv2.warpAffine(img, M, (w, h), borderValue=(255,255,255))
        else:
            rotated = img

        # OCR
        results = reader.readtext(rotated, detail=0)

        # check có chữ "m3" hoặc "m³"
        text = " ".join(results).lower()
        print(f"Angle: {angle}, Detected text: {text}")
        if "m3" in text or "m³" in text:
            score = len(text)  # đơn giản lấy độ dài text làm điểm
            if score > best_score:
                best_score = score
                best_angle = angle
                best_text = text

    display(rotated, f"Detected Text at {best_angle} degrees")
    return best_angle, best_text

