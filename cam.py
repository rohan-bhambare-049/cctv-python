import cv2
import time
import datetime

cap = cv2.VideoCapture(0) # Video Capture Device

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 5

frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")

while True:
    _, frame = cap.read()

    # Converting the Image into Greay Scale Image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # It Returns the Various Positions of the faces
    #                   for faces -------------> ^ This Number should be between 1.0 to 1.5 (Name = Scale Factor)
    #                                              The Lower the Number goes the More Accurate It gets
    bodies = body_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) + len(bodies) > 0:
        if detection:
            timer_started = False
        else:
            detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20, frame_size)
            print("Started Recording!")
    elif detection:
        if timer_started:
            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False
                timer_started = False
                out.release()
                print("Stopped and Saved the Recording!")
        else:        
            timer_started = True
            detection_stopped_time = time.time() # This gives the Current Time

    for (x,y,width,height) in faces:
        cv2.rectangle(frame, (x,y), (x+width,y+height), (255,0,0), 1) # The Color is in BGR
    for (x,y,width,height) in bodies:
        cv2.rectangle(frame, (x,y), (x+width,y+height), (255,0,0), 1) # The Color is in BGR    

    if detection:
        out.write(frame)

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()


























