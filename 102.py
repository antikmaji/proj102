import cv2
import dropbox
import time
import random

start_time=time.time()


def take_snapshot():

    number=random.randint(0,100)

    videoCaptureObject=cv2.VideoCapture(0)

    result=True

    while(result):
        ret,frame=videoCaptureObject.read()

        img_name="Img"+str(number)+".png"

        cv2.imwrite(img_name,frame)

        start_time=time.time

        result=False

    return img_name

    print("Snapshot taken")

    videoCaptureObject.release()

    cv2.destroyAllWindows()

def Upload_File(img_name):

    access_token="sl.BMdE3S5jaMGa9TDnmdCeHFAskwa-Mf2-D01WXd3gy5Te7P_rXrNfjICSlT7Gy7vPRfoHqQhKHzwe9Tx80B0grb8bM30Cu8zyQErnKLMsMDX3Q9V98VLCoHZgBth3ELquL4p39UU"

    file=img_name
    file_from=file
    file_to="/newFolder1/"+img_name

    dbx=dropbox.Dropbox(access_token)

    with open(file_from,"rb") as f:

        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)

        print("File Uploaded")

def main():

    while(True):
        if ((time.time()-start_time)>=300):
            name=take_snapshot()

            Upload_File(name)
main()

