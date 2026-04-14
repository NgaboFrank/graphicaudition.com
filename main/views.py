from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

BASE_CONTEXT = {
    "brand_name": "Graphic Audition",
    "phone_display": "0784 330 484",
    "phone_link": "250784330484",
    "email": "graphicaudition@gmail.com",
    "instagram_url": "https://www.instagram.com/graphic_auditions?igsh=MXB5NjlzZmp4NzAwcw==",
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
        {"name": "Rooted Institute Campaign", "desc": "Uploaded portfolio work added to your final site.", "image": "main/images/rooted-institute-1.jpg"},
        {"name": "Rooted Institute Poster", "desc": "Uploaded portfolio work added to your final site.", "image": "main/images/rooted-institute-2.jpg"},
        {"name": "Nova Skills Flyer", "desc": "Uploaded portfolio work added to your final site.", "image": "main/images/nova-skills.jpg"},
    ],
    "stats": [
        {"number": "21+", "label": "Creative Samples"},
        {"number": "6+", "label": "Premium Services"},
        {"number": "24/7", "label": "Fast Response"},
    ],
    "reasons": [
        {"title": "Innovative strategies", "text": "We combine bold ideas and modern design direction so brands stand out."},
        {"title": "Results that matter", "text": "Our visuals are made to improve presentation, trust, and engagement."},
        {"title": "Tailored solutions", "text": "Each project is shaped around your brand goals and audience."},
        {"title": "Client centered approach", "text": "We listen carefully, revise clearly, and keep the process professional."},
    ],
    "packages": [
        {
            "title": "Starter Package",
            "tag": "Best for startups",
            "features": ["Logo design", "Brand color direction", "Social media post set", "Flyer or poster design"],
            "cta": "Get Started",
            "featured": False,
        },
        {
            "title": "Professional Package",
            "tag": "Most requested",
            "features": ["Brand identity design", "Marketing materials design", "Website design", "Social media content support", "Revision support"],
            "cta": "Get a Consultation",
            "featured": True,
        },
        {
            "title": "Essential Package",
            "tag": "Ongoing support",
            "features": ["Monthly social media design", "Brand consistency support", "Campaign creative updates", "Fast delivery workflow"],
            "cta": "Subscribe Now",
            "featured": False,
        },
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
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        service = request.POST.get("service", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not email or not message:
            messages.error(request, "Please fill in your name, email, and message.")
            return render(request, "main/contact.html", ctx)

        full_message = f"""
New contact form message from Graphic Audition website

Name: {name}
Email: {email}
Phone: {phone}
Service Needed: {service}

Message:
{message}
"""
        try:
            send_mail(
                subject=f"Graphic Audition Contact: {name}",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_RECEIVER_EMAIL],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully.")
            return redirect("contact")
        except Exception as exc:
            messages.error(request, f"Email error: {exc}")
            return render(request, "main/contact.html", ctx)

    return render(request, "main/contact.html", ctx)
