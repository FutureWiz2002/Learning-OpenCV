import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = cv.imread('sunset-illustration-6000x4000-12659.jpg', cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"
# edges = cv.Canny(img,100,200)
# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()


cap = cv2.VideoCapture(0)
    
# while True: 
    
#     ret,img=cap.read()
    
#     cv2.imshow('Video', img)
    
#     if(cv2.waitKey(10) & 0xFF == ord('b')):
#         break

frameno = 0
while(True):
   ret,frame = cap.read()
   if ret:
      # if video is still left continue creating images
      name = str(frameno) + '.jpg'
      print ('new frame captured...' + name)

      cv2.imwrite(name, frame)
      frameno += 1
   else:
      break
 
cap.release()
cv2.destroyAllWindows()


