Graphic Audition email setup

1. Log into graphicaudition@gmail.com
2. Turn on 2-Step Verification in Google Account security
3. Open https://myaccount.google.com/apppasswords
4. Generate a Mail app password
5. Put the 16-character password into Render Environment as EMAIL_HOST_PASSWORD
6. Redeploy your Render service

Environment values you need on Render:
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=graphicaudition@gmail.com
EMAIL_HOST_PASSWORD=YOUR_GMAIL_APP_PASSWORD
DEFAULT_FROM_EMAIL=graphicaudition@gmail.com
CONTACT_RECEIVER_EMAIL=graphicaudition@gmail.com
