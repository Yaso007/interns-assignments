import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

# Configuration
EMAIL = sender_email = "yashopmukhiazz007@gmail.com"  # Replace with your email
  # Replace with your email
PASSWORD = "Yashop@Thisismypassword"  # Replace with your email password
TO_EMAIL = "yusufmukhia@gmail.com"
IMAGE_PATH = "path_to_your_image.png"  # Replace with the image file path

# Email details
subject = "Challenge 3 Completed"
body = """
Hello,

This is to inform you that I have completed Challenge 3.

Details:
Name: Your Name
Semester: Your Semester
Branch: Your Branch
Roll Number: Your Roll Number

Best regards,
Your Name
"""

# Validate image
if not os.path.isfile(IMAGE_PATH) or os.path.splitext(IMAGE_PATH)[-1].lower() not in [".png", ".jpg", ".jpeg"]:
    raise FileNotFoundError("Invalid image file. Only PNG, JPG, and JPEG files are allowed.")

# Create email
msg = MIMEMultipart()
msg['From'] = EMAIL
msg['To'] = TO_EMAIL
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Attach image
with open(IMAGE_PATH, 'rb') as img_file:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(img_file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(IMAGE_PATH)}')
    msg.attach(part)

# Send email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.send_message(msg)
    print("Email sent successfully!")
