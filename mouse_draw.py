import numpy as np
import cv2

img=np.zeros((1024,1024,3),np.uint8)
img.fill(255)
cv2.namedWindow('Lets Draw')

drawing=False
mode=True
(ix,iy)=(-1,-1)

def draw_circle(event,x,y,flags,param):    
    global ix,iy,drawing,mode
    
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        (ix,iy)=x,y
        
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            if mode==True:
                cv2.rectangle(img,(x,y),(0,0,255),-1)
            else:
                cv2.circle(img,(x,y),5,(100,255,100),-1)
                
    elif event==cv2.EVENT_LBUTTONUP:
            drawing=False
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(255,255,0),4)
                
            else:
                cv2.circle(img,(x,y),5,(0,0,255),4)
                

cv2.setMouseCallback('Lets Draw',draw_circle)

def main():
    global mode
       
    while(True):
        cv2.imshow('Lets Draw',img)
        k=cv2.waitKey(1)
        if k==ord('m') or k==ord('M'):
           mode=not mode
        elif k==ord('q'):
             break
          
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()

         
