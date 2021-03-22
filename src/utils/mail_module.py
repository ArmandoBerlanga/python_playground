import smtplib
from email.message import EmailMessage

sender_mail = "****"
password = "***"

def send_simple (subject : str, body : str):
    with smtplib.SMTP ("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(sender_mail, password)

        msg = f"Subject: {subject}\n\n{body}"

        smtp.sendmail(sender_mail, "Armandoberlanga2708@gmail.com", msg)

def send_complex (receiver_mail : str, subject : str, body : str, attach : bool, files):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_mail
    msg["To"] = receiver_mail
    msg.set_content(body)

    if attach:
        for file in files:
            with open (file, "rb") as f:
                file_data = f.read()

                st = file.split("/")
                file_name = st[len(st)-1]

            msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

    with smtplib.SMTP_SSL ("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_mail, password)
        smtp.send_message(msg)