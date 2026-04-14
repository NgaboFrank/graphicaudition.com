1. Upload project to GitHub or Render.
2. In Render Environment add:
   EMAIL_HOST_USER=graphicaudition@gmail.com
   EMAIL_HOST_PASSWORD=YOUR_GMAIL_APP_PASSWORD
   DEFAULT_FROM_EMAIL=graphicaudition@gmail.com
   CONTACT_RECEIVER_EMAIL=graphicaudition@gmail.com
3. Deploy latest commit.
4. If you add a custom domain, add it to ALLOWED_HOSTS_EXTRA and CSRF_TRUSTED_ORIGINS_EXTRA.
