import cv2 as cv
import  numpy as np

#this code is for edg detection taking single pic.
'''img=cv.imread('a1.jpg')    #reading image from secondry storage.
cv.imwrite('RG.jpg',img)       #writting this image as new image.
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)  #changing colors frames

cv.imwrite('BG.jpg',img)  #now saving the copy of BGR image to RGB.
img=cv.cvtColor(img,cv.COLOR_RGB2GRAY)   #converting RGB to Grray frames.

cv.imwrite('Gry.jpg',img)    #re-writting grray-frame image.

img=cv.Canny(img,threshold1=100,threshold2=100)   #Dedecting edges on boundary(thresold1) and 
#inside boundary(thresold2) image.
cv.imwrite('Edge.jpg',img)
cv.imshow('Edge.jpg',img)
cv.waitKey(0)
cv.destroyAllWindows()'''

#live edging detection
cap=cv.VideoCapture(0)   #opening web cam live to taake image.
while True:
    _,img=cap.read()     #reading live image and saving it two variable.
    img=cv.cvtColor(img,cv.COLOR_BGR2RGB)    #Converting frames into RGB.
    img=cv.cvtColor(img,cv.COLOR_RGB2GRAY)   #converting frames into grray scales.

    img=cv.Canny(img,threshold1=50,threshold2=100)    #edging from boundary and inside boundary.
    cv.imshow('Egde',img)                             #displaying the window
    if(cv.waitKey(1) & 0xFF == ord('q')):             #for contenue the window
        break
cap.release()
cv.destroyAllWindows()