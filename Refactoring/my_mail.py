import email
import imaplib
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv


class MyMail:
    def __init__(self, PASSWORD, FROM):
        self.FROM = FROM
        self.PASSWORD = PASSWORD
        self.TO = ["vasya@email.com", "petya@email.com"]
        self.SUBJECT = "Subject"
        self.GMAIL_SMTP = "smtp.gmail.com"
        self.GMAIL_IMAP = "imap.gmail.com"

    def make_message(self, message):
        new_message = MIMEMultipart()
        new_message["From"] = self.FROM
        new_message["To"] = ", ".join(self.TO)
        new_message["Subject"] = self.SUBJECT

        new_message.attach(MIMEText(message))

    def send_message(self, message):
        server = smtplib.SMTP(self.GMAIL_SMTP, 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.FROM, self.PASSWORD)
        server.sendmail(
            self.FROM, server, self.make_message(message).as_string()
        )
        server.quit()

    def recieve_message(self, header=None):
        current_mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        current_mail.login(self.FROM, self.PASSWORD)
        current_mail.list()
        current_mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else "ALL"
        _, data = current_mail.uid("search", None, criterion)
        assert data[0], "There are no letters with current header"
        latest_email_uid = data[0].split()[-1]
        _, letter = current_mail.uid("fetch", latest_email_uid, "(RFC822)")
        raw_email = letter[0][1]
        email_message = email.message_from_string(raw_email)
        current_mail.logout()
        return email_message


if __name__ == "__main__":
    load_dotenv()
    PASSWORD = os.getenv("PASSWORD")
    FROM = os.getenv("FROM")
    message = "Message"

    person = MyMail(PASSWORD, FROM)
    person.send_message(message)
    person.recieve_message()
