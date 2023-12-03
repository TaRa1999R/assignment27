
import cv2

img = cv2.imread ("3_input.jpg")
img = cv2.cvtColor (img , cv2.COLOR_BGR2GRAY)
rows , cols = img.shape
writer = cv2.VideoWriter ("3_output.mp4" , cv2.VideoWriter_fourcc(*'mpv4') , 10 , (cols , rows))

while True :
    

    cv2.imshow ("result 3" , img)
    if cv2.waitKey (25) & 0xFF == ord ('q') :
        break
