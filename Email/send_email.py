__author__ = 'MissMaximas'

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from jinja2 import Environment, PackageLoader

import smtplib

SMTP_SERVER_HOST = "127.0.0.1" # Use your SMTP server details
SMTP_SERVER_PORT = 11 # Use your SMTP server details
FROM_EMAIL_ADDRESS = "test@test.com"

to_email_addresses = [FROM_EMAIL_ADDRESS]

msg = MIMEMultipart()
msg['From'] = FROM_EMAIL_ADDRESS
msg['To'] = COMMASPACE.join(to_email_addresses)
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = "TEST"

message = {"test": "Test Message"}
template_name = 'my_first_template.html'

env = Environment(loader=PackageLoader('Email', 'data'))
template = env.get_template(template_name)
content = template.render(message)

msg.attach(MIMEText(content, 'html'))

try:
    print("Sending emails to: " + ", ".join(to_email_addresses))
    server = smtplib.SMTP(SMTP_SERVER_HOST, SMTP_SERVER_PORT)
    server.sendmail(FROM_EMAIL_ADDRESS, to_email_addresses, msg.as_string())
    server.quit()
except Exception as e:
    print(e)



