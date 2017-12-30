import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = "cmshivam01998@gmail.com"
toaddr = "pratiush309@gmail.com"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "PythonTesting"
 
body = "First mail with attachment"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "manual.pdf"
attachment = open("C:\Users\Asus\Desktop\manual.pdf", "rb")
 
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
server.quit()
