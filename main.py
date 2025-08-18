from controller import *

img_path = 'main.png'

def main():
    img = rotate.img_rotate(img_path)
    ocr.detect_orientation(img)


if __name__ == "__main__":
    main()