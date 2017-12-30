import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("shivam01998@gmail.com", "*************")
 
msg = "Hey bro this is my first mail by a python script"
server.sendmail("shivam01998@gmail.com", "camds01998@gmail.com", msg)
server.quit()
