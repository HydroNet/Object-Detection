# Rafael Almazar
# CSUN DMSP
# Fall 2021

# Purpose: Used for taking pictures and recording video.
# Note: Inputs are not checked because this is for demo purposes only.

import os
import time

def main():
    choice = input("(P)icture or (V)ideo:\n")
    while (choice != 'P' or choice != 'p' or choice != 'V' or choice != 'v'):
        if choice == 'P' or choice == 'p':
            capturePic()
            break
        elif choice == 'V' or choice == 'v':
            captureVideo()
            break
        else:
            print("Invalid input, enter 'p' or 'v'.")
            choice = input("(P)icture or (V)ideo:\n")
    
def capturePic():
    numPics = int(input("Enter number of pictures: "))
    totalElapsedTime = 0
    
    for i in range(numPics):
        start = time.time()
        print("Capturing picture %d..." % (i + 1))
        cmd = "raspistill -o test_%d.jpg --timeout 1" % (i + 1)
        os.system(cmd)
        end = time.time()
        totalElapsedTime += end - start
        print("Picture %d done." % (i + 1))
        
    averageCaptureTime = totalElapsedTime / numPics
    print("\nAll done!")
    print("Average Capture Time: %d" % averageCaptureTime)
    
def captureVideo():
    time = int(input("Enter number of seconds:"))
    time *= 1000 # convert to ms
    cmd = "raspivid -o video.h264 -t %d" % time
    os.system(cmd)
    print("Video done.")

if __name__ == "__main__":
    main()

