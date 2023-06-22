import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email=input("Enter sender email: ")
sender_password=input("Enter sender email's password: ")
recipient_email=input("Enter recipient email: ")
subject=input("Enter subject:")
message=input("Enter message: ")

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Create a MIME multipart message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject

    # Attach the message to the email
    msg.attach(MIMEText(message, "plain"))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Log in to the sender's email account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully!")

        # Disconnect from the server
        server.quit()
    except smtplib.SMTPException as e:
        print("Error sending email:", str(e))

send_email(sender_email, sender_password, recipient_email, subject, message)