HOW TO MAKE THE CONTACT FORM SEND EMAIL ON RENDER

1. Go to your Gmail account security settings.
2. Turn on 2-Step Verification.
3. Create a Gmail App Password.
4. In Render, open your service -> Environment.
5. Add these values:
   EMAIL_HOST_USER=graphicauditions@gmail.com
   EMAIL_HOST_PASSWORD=your_gmail_app_password
6. Redeploy the service.

The website form will then send messages to:
graphicauditions@gmail.com
