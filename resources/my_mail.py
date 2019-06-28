"""A simple mail interface for sending email with optional attachment
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

def send_mail(send_from, send_to, subject, text, server, port, password='', att=None, ):
    """A simple mail interface for sending mail with attachments

    Arguments:
        send_from {str} -- The user display name, and email address to send from
        send_to {str} -- Email address to send to
        subject {str} -- the subject of the email
        text {str} -- the body of the email
        server {str} -- the mail server
        port {int} -- the port number

    Keyword Arguments:
        password {str} -- the email account password (default: {''})
        att {str} -- path to attached document (default: {None})
    """

    msg = MIMEMultipart()
    # from is display name
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    part = MIMEBase('application', "octet-stream")
    if att:
        part.set_payload(open(att, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename='+subject)
        msg.attach(part)
    smtp = smtplib.SMTP_SSL(server, port)
    # login must be the email address
    smtp.login(send_from, password)
    smtp.sendmail(send_from, [send_to], msg.as_string())
    smtp.quit()
