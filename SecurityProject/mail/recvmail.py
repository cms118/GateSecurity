import imaplib
import email
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('cmshivam01998@gmail.com', '*********')
mail.list()

mail.select("inbox") # connect to inbox.
 #Get an email
result, data = mail.uid('fetch', b'1', '(RFC822)')

raw_email = data[0][1]
email_message = email.message_from_string(raw_email)

print email_message['To']

print email.utils.parseaddr(email_message['From']) # for parsing "Yuji Tomita" <yuji@grovemade.com>

print email_message.items() # print all headers


def get_first_text_block(self, email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload()
