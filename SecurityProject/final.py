import cv2
import numpy as np
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import time
import imaplib
import email
import datetime
import pyttsx
import threading
import thread


EMAIL_ACCOUNT = "cmshivam01998@gmail.com"
PASSWORD = "*********"

cms = 0;
pratiush=0;
unknown=0;
count = 0;
c = 0;

def mail(str):
    fromaddr = "cmshivam01998@gmail.com"
    toaddr = "shivam01998@gmail.com"
     
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
    server.login(fromaddr, "accountFORpython")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    print "mail sent"
    server.quit()


def tts(str):
    engine = pyttsx.init()
    engine.say(str)
    engine.runAndWait()

def mail1():
    print "cms"
    time.sleep(1)
    global count
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(EMAIL_ACCOUNT, PASSWORD)
    mail.list()
    mail.select('inbox')
    result, data = mail.uid('search', None, "UNSEEN") # (ALL/UNSEEN)
    i = len(data[0].split())

    for x in range(i):
        latest_email_uid = data[0].split()[x]
        result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = email_data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)

        # Header Details
        date_tuple = email.utils.parsedate_tz(email_message['Date'])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
            local_message_date = "%s" %(str(local_date.strftime("%a, %d %b %Y %H:%M:%S")))
        email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))
        email_to = str(email.header.make_header(email.header.decode_header(email_message['To'])))
        subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))

        # Body details
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                print email_from
                if email_from == "Shivam Kumar <shivam01998@gmail.com>":
                    print body
                    if(body.startswith('Yes')):
                        tts('Gate is opening , have patience')
                        count = 0
                        break
                    else:
                        count = 0
                        tts ('Sorry You are not allowed to come now')
                        break
            else:
                continue



def processing():
    global count
    global cms
    global pratiush
    global unknown
    global c
    recognizer = cv2.createLBPHFaceRecognizer()
    recognizer.load('trainner/trainner.yml')
    cascadePath = "frontface.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);


    cam = cv2.VideoCapture(0)
    font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 5, 1, 0, 1, 1)
    while True:
        if (cms >= 10 or pratiush >= 10) and count == 0 :
            count = 1
            th2 = threading.Thread(target = mail , args = ("cms",))
            th2.start()
            th2.join()
            cms = 0
            pratiush = 0
        elif unknown >= 50 and count == 0 :
            count = 1
            th2 = threading.Thread(target = mail , args = ("unknown",))
            th2.start()
            th2.join()
            unknown = 0
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
            #cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font, 255)
        if(c==10):
            cv2.imwrite("C:\Users\Asus\Desktop\User.jpg",im)
        c+=1
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()


th = threading.Thread(target = processing)
th1 = threading.Thread(target = mail1)
th.start()
th1.start()
th.join()

th1.join()




    
    
