import smtplib
import time
import imaplib
import email
import datetime

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "cmshivam01998" + ORG_EMAIL
FROM_PWD    = "**********"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993


date = (datetime.date.today() - datetime.timedelta(1)).strftime("%d-%b-%Y")
#result, data = mail.uid('search', None, '(SENTSINCE {date})'.format(date=date))


def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        

        type, data = mail.uid('search', None,'(SENTSINCE {date} HEADER FROM "shivam01998@gmail.com")'.format(date=date))
        mail_ids = data[0]

        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(i, '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print 'From : ' + email_from 
                    print 'Subject : ' + email_subject
                    print  str(email.header.make_header(email.header.decode_header(email_message['Subject'])))

    except Exception, e:
        print str(e)
while(1):
    read_email_from_gmail()
    time.sleep(5);
    print "cms"


