from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render

BASE_CONTEXT = {
    "brand_name": "Graphic Audition",
    "phone_display": "0784 330 484",
    "phone_link": "250784330484",
    "instagram_url": "https://www.instagram.com/graphic_auditions?igsh=MXB5NjlzZmp4NzAwcw==",
    "contact_email": "graphicauditions@gmail.com",
    "services": [
        {"title": "Brand Identity", "text": "Logo systems, color direction, and premium brand presentation for businesses that want to look serious."},
        {"title": "Social Media Design", "text": "Creative posts, campaign visuals, and promotional content that make your page look stronger."},
        {"title": "Flyer & Poster Design", "text": "Clean, bold flyer layouts for events, products, services, and announcements."},
        {"title": "Web Design", "text": "Modern websites that present your work professionally and help people trust your brand."},
        {"title": "Mockups & Presentation", "text": "Premium mockups and brand previews that make your design work feel polished."},
        {"title": "Campaign Visuals", "text": "Launch creatives, offer promotions, and ad-ready visuals built to attract attention."},
    ],
    "portfolio": [
        {"name": "Mango 4G Campaign", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/mango-4g.jpg"},
        {"name": "BetPawa Campaign", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/betpawa-campaign.jpg"},
        {"name": "Crypto Poster", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/crypto-top-coins.jpg"},
        {"name": "Bonsoir Evening Visual", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/bonsoir-evening.jpg"},
        {"name": "Bonsoir Friday Post", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/bonsoir-friday.jpg"},
        {"name": "Bonsoir Table Visual", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/bonsoir-table.jpg"},
        {"name": "Bonsoir Eid Design", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/bonsoir-eid.jpg"},
        {"name": "Bonsoir Lifestyle Design", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/bonsoir-lifestyle.jpg"},
        {"name": "Creative Flyer", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/ga-creative-flyer.jpg"},
        {"name": "Dress With Nice Ad", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/dresswithnice.jpg"},
        {"name": "Cent Mockup", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/cent-mockup.jpg"},
        {"name": "Beyond Limits Creative", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/beyond-limits.jpg"},
        {"name": "Happy December Design", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/happy-december.jpg"},
        {"name": "KBVS Flyer", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/kbvs-cleaning.jpg"},
        {"name": "Cent Logo Presentation", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/cent-logo.jpg"},
        {"name": "Nova Mockup", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/nova-brand.jpg"},
        {"name": "Monday Motivation Post", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/monday-started.jpg"},
        {"name": "New Week Graphic", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/new-week.jpg"},
    ],
    "stats": [
        {"number": "18+", "label": "Creative Samples"},
        {"number": "6+", "label": "Premium Services"},
        {"number": "24/7", "label": "Fast Response"},
    ],
    "reasons": [
        {"title": "Innovative strategies", "text": "We combine bold ideas and modern design direction so brands stand out."},
        {"title": "Results that matter", "text": "Our visuals are made to improve presentation, trust, and engagement."},
        {"title": "Tailored solutions", "text": "Each project is shaped around your brand goals and audience."},
        {"title": "Client centered approach", "text": "We listen carefully, revise clearly, and keep the process professional."},
    ],
    "testimonials": [
        {"name": "Client Review", "text": "Excellent work from concept to final delivery. The design quality felt premium and the communication stayed clear."},
        {"name": "Business Owner", "text": "Our business looked more professional immediately. The final visuals gave us a stronger first impression."},
        {"name": "Marketing Client", "text": "The work was clean, modern, and ready to use. It matched the brand direction perfectly."},
    ],
}


def _ctx(page_title):
    ctx = dict(BASE_CONTEXT)
    ctx["page_title"] = page_title
    return ctx


def home(request):
    return render(request, "main/home.html", _ctx("Home"))


def portfolio(request):
    return render(request, "main/portfolio.html", _ctx("Portfolio"))


def services(request):
    return render(request, "main/services.html", _ctx("Services"))


def about(request):
    return render(request, "main/about.html", _ctx("About"))


def contact(request):
    ctx = _ctx("Contact")

    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        service = request.POST.get("service", "").strip()
        message = request.POST.get("message", "").strip()

        ctx["form_values"] = {
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "service": service,
            "message": message,
        }

        if not full_name or not email or not message:
            messages.error(request, "Please fill in your name, email, and message.")
            return render(request, "main/contact.html", ctx)

        subject = f"Graphic Audition Website Inquiry - {full_name}"
        body = (
            "New message from the Graphic Audition contact form.\n\n"
            f"Full Name: {full_name}\n"
            f"Email: {email}\n"
            f"Phone: {phone or 'Not provided'}\n"
            f"Service Needed: {service or 'Not selected'}\n\n"
            "Message:\n"
            f"{message}\n"
        )

        try:
            mail = EmailMessage(
                subject=subject,
                body=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_RECEIVER_EMAIL],
                reply_to=[email],
            )
            mail.send(fail_silently=False)
            messages.success(request, "Your message was sent successfully. We will reply soon.")
            return redirect("contact")
        except Exception:
            messages.error(request, "Email is not configured yet. Add your Gmail settings on Render first.")
            return render(request, "main/contact.html", ctx)

    ctx["form_values"] = {
        "full_name": "",
        "email": "",
        "phone": "",
        "service": "",
        "message": "",
    }
    return render(request, "main/contact.html", ctx)
