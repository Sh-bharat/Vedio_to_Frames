#Bharat Sharma 23MDT1051
import cv2
import os
import time

input_video = input("Enter the path to the input video file: ")
output_directory = input("Enter the path to the output directory: ")

if not os.path.isfile(input_video):
    print(f"Error: Input video file '{input_video}' does not exist.")
    exit()

if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    print(f"Created output directory: {output_directory}")

vidcap = cv2.VideoCapture(input_video)
fps = vidcap.get(cv2.CAP_PROP_FPS)
frame_interval = int(fps)

success, image = vidcap.read()
count = 0

while success:
    frame_filename = os.path.join(output_directory, f"frame{count}.jpg")
    cv2.imwrite(frame_filename, image)

    if not os.path.isfile(frame_filename):
        print(f"Error: Failed to save frame {count}.")
        exit()

    for i in range(frame_interval):
        success, image = vidcap.read()

    print(f"Saved frame {count} to {frame_filename}")
    count += 1

vidcap.release()
