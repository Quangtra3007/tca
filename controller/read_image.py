import os
import cv2

pic_left = "left.jpg"
pic_right = "right.jpg"
temp_dir = "./../template/"

def take_pic():
    result = True
    status1= os.WEXITSTATUS(os.system(f"fswebcam -d /dev/video0 -r 640x480 --no-banner {temp_dir}/{pic_left}"))
    print(status1)
    status2 =os.WEXITSTATUS(os.system("fswebcam -d /dev/video1 -r 640x480 --no-banner {temp_dir}/{pic_right}"))
    print(status2)
    if status1 ==0 and status2==0:   
        print("Failed to take picture")
        result = False  
    else:
        print("Picture taken successfully")
    return result

def divide_image():
    # Load image
    img = cv2.imread(f"{temp_dir}/{pic_left}")
    h, w, _ = img.shape

    # Decide how to split: 2 rows × 4 columns = 8 parts
    rows, cols = 2, 4
    part_h, part_w = h // rows, w // cols

    count = 0
    for i in range(rows):
        for j in range(cols):
            y1, y2 = i * part_h, (i + 1) * part_h
            x1, x2 = j * part_w, (j + 1) * part_w
            crop = img[y1:y2, x1:x2]
            out_name = os.path.join(temp_dir, f"part_{count+1}.jpg")
            cv2.imwrite(out_name, crop)
            print(f"Saved {out_name}")
            count += 1

    print("Done! Split into 8 equal images.")


if __name__ == "__main__":
    take_pic()
    divide_image()
