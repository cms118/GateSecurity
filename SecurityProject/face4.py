import cv2
import numpy as np
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load('trainner/trainner.yml')
cascadePath = "frontface.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

cms = 0;
pratiush=0;
unknown=0;

def mail(str):
    fromaddr = "cmshivam01998@gmail.com"
    toaddr = "pratiush309@gmail.com"
     
    msg = MIMEMultipart()
     
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "ProjectCms"
     
    body = "Have a look at this Someone has arrived on the gate"+str
     
    msg.attach(MIMEText(body, 'plain'))
     
    filename = "User.jpg"
    attachment = open("C:\Users\Asus\Desktop\User.jpg", "rb")
     
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    msg.attach(part)
     
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "***********")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    print "mail sent"
    server.quit()

c=0;

cam = cv2.VideoCapture(1)
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 5, 1, 0, 1, 1)
while True:
    if cms == 10 or pratiush == 10:
        mail("cms")
        break
    elif unknown == 100:
        mail("unknown")
        break
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        if(conf<50):
            if(Id==1):
                cms+=1;
                Id="cms"
            elif(Id==2):
                pratiush+=1
                Id="Jagadeesh"
        else:
            Id="Unknown"
            unknown+=1
        cv2.imshow("img",im)
        cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font, 255)
    if(c==10):
        cv2.imwrite("C:\Users\Asus\Desktop\User.jpg",im)
    c+=1
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
