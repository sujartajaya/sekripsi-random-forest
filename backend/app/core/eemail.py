import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.core.settings import settings


def send_email(
    to_email: str,
    subject: str,
    html: str
):

    msg = MIMEMultipart()

    msg["From"] = settings.SMTP_FROM
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(
        MIMEText(
            html,
            "html"
        )
    )

    server = smtplib.SMTP(
        settings.SMTP_HOST,
        settings.SMTP_PORT
    )

    server.starttls()

    server.login(
        settings.SMTP_USERNAME,
        settings.SMTP_PASSWORD
    )

    server.sendmail(
        settings.SMTP_FROM,
        to_email,
        msg.as_string()
    )

    server.quit()