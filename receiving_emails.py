import imaplib

m = imaplib.IMAP4_SSL('imap.gmail.com')

import getpass

email = getpass.getpass('Email please:')
password = getpass.getpass('Password please:')

m.login(email,password)

m.list()

m.select('inbox')

typ, data = m.search(None, 'SUBJECT "NEW TEST PYTHON"')

email_id = data[0]

result, email_data = m.fetch(email_id, 'RFC822')

# email_data

raw_email = email_data[0][1]

raw_email_string = raw_email.decode('utf-8')

import email

email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():

    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        print(body)

