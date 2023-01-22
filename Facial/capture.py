import cv2
import time
import os
# Initialize the camera
cam = cv2.VideoCapture(0)

# Create a directory to store the images
dataset_path = 'datasets/'
if not os.path.exists(dataset_path):
    os.mkdir(dataset_path)

# Get the name of the person you're capturing images of
name = input("Enter the name of the person: ")
folder_path = dataset_path + name
if not os.path.exists(folder_path):
    os.mkdir(folder_path)

# Capture 5 images
count = 0
while count < 100:
    ret, frame = cam.read()
    img_path = folder_path + '/' + name + '_' + str(count) + '.jpg'
    cv2.imwrite(img_path, frame)
    print("{} written!".format(img_path))
    time.sleep(0.1) # wait for 1 second
    count += 1

# Release the camera and close the window
cam.release()
cv2.destroyAllWindows()
