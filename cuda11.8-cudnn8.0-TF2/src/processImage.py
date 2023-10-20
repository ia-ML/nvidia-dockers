import os, sys, cv2
import cv2.cuda as cvg
import argparse
import numpy as np   
from pathlib import Path

### "1">Black and White<
def processBW(image, isGPU=0):    
    output_image = None
    if isGPU:
        _, thresholded_image = cv2.cuda.threshold(image, 127, 255, cv2.THRESH_BINARY)
        output_image = thresholded_image.download()
    else:
       output_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    return output_image



def main(inputImagePath, outputImagePath, processType, isGPU=0 ):

    #Save the current working directory
    original_cwd = os.getcwd()
        
    if processType == "1":
        print("OpenCV Process.....")         
        image = cv2.imread(inputImagePath)
        if image is None:
            print('Could not open or find the image')
            exit(0)
        output_image = None
        # these processings required gray images 
        print("Black and white" )
        output_image = processBW(output_image)[1]
    elif processType =="2": 
        processArgs = ""
        pyPath = "./dnn-code/someDNNProcess.py"

        cmd = "python3 "+pyPath+" " + inputImagePath + " " + outputImagePath  + processArgs  
        print(cmd)             
        os.system(cmd) 

if __name__ == "__main__":

    # Check the OpenCV version
    print("OpenCV version: ", cv2.__version__)
    # Check if CUDA is available
    print("Number of GPUs: ", cv2.cuda.getCudaEnabledDeviceCount())

    parser = argparse.ArgumentParser(description="Process image using GPU")
    parser.add_argument("inputImagePath", help="Path to the input image file")
    parser.add_argument("outputImagePath", help="Path to the output image file")
    parser.add_argument("processType", help=" type of process")
    
    # # # Parse the command-line arguments
    args = parser.parse_args()
    print(args)
    # #Call the main function with the input image path\
    args.inputImagePath  = os.path.join(os.getcwd(), args.inputImagePath)
    args.outputImagePath = os.path.join(os.getcwd(), args.outputImagePath)
    main(args.inputImagePath, args.outputImagePath, args.processType)
    
    print("image processing is completed")
