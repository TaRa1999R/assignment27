
import cv2

cap = cv2.VideoCapture (0)
# writer = cv2.VideoWriter ("4_output.mp4" , cv2.VideoWriter_fourcc(*'mpv4') , 10 , (480 , 640))

while True :
    _ , fram = cap.read ()
    fram = cv2.cvtColor (fram , cv2.COLOR_BGR2GRAY)
    # print (fram.shape)      -->   (480 , 640)
    cv2.rectangle (fram , (260 , 180) , (380 , 300) , (255 , 255 , 255) , 2)
    check_color = fram[179:302 , 259:382]
    blur_fram = cv2.blur (fram, (30 , 30))
    blur_fram[179:302 , 259:382] = check_color

    cv2.imshow ("result 4" , blur_fram)
    # writer.write (img)
    if cv2.waitKey (25) & 0xFF == ord ('q') :
        break
# cap.release()
# writer.release ()