
import random
import cv2

img = cv2.imread ("3_input.jpg")
img = cv2.cvtColor (img , cv2.COLOR_BGR2GRAY)
rows , cols = img.shape
writer = cv2.VideoWriter ("3_output.mp4" , cv2.VideoWriter_fourcc(*'mpv4') , 10 , (cols , rows))
snow_place = []

while True :
    snow_img = img
    new_snow = random.randint (0 , cols)
    snow_place.append ({"row" : 0 , "col" : new_snow})
    for snow in snow_place :
        cv2.circle (snow_img , (snow["col"] , snow["row"]) , 3 , (255 , 255 , 255) , -1)
        snow["row"] += 8

        if snow["row"] >= rows :
            snow_place.remove (snow)

    cv2.imshow ("result 3" , img)
    if cv2.waitKey (100) & 0xFF == ord ('q') :
        break
