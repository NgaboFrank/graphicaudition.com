
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

BASE_CONTEXT = {
    "brand_name": "Graphic Audition",
    "phone_display": "0784 330 484",
    "phone_link": "250784330484",
    "contact_email": "graphicaudition@gmail.com",
    "instagram_handle": "@graphic_auditions",
    "instagram_url": "https://www.instagram.com/graphic_auditions?igsh=MXB5NjlzZmp4NzAwcw==",
    "services": [
        {"title": "Brand Identity", "text": "Logo systems, color direction, and premium brand presentation for businesses that want to look serious."},
        {"title": "Social Media Design", "text": "Creative posts, campaign visuals, and promotional content that make your page look stronger."},
        {"title": "Flyer & Poster Design", "text": "Clean, bold flyer layouts for events, products, services, and announcements."},
        {"title": "Web Design", "text": "Modern websites that present your work professionally and help people trust your brand."},
        {"title": "Mockups & Presentation", "text": "Premium mockups and brand previews that make your design work feel polished."},
        {"title": "Campaign Visuals", "text": "Launch creatives, offer promotions, and ad-ready visuals built to attract attention."},
    ],
    "packages": [
        {
            "title": "Starter Package",
            "subtitle": "Perfect for startups & small businesses.",
            "items": ["Logo Design", "Brand Style Guide", "Social Media Templates (3)", "Marketing Material Kit"],
            "note": "One-Time Creative Setup",
            "cta": "GET STARTED",
            "featured": False,
        },
        {
            "title": "Professional Package",
            "subtitle": "Comprehensive branding & marketing support.",
            "items": ["Brand Identity Design", "Marketing Materials Design", "Social Media Management", "Website Design and Development", "SEO & Web Maintenance"],
            "note": "Setup + Ongoing Support",
            "cta": "GET A CONSULTATION",
            "featured": True,
        },
        {
            "title": "Essential Package",
            "subtitle": "Ongoing social media & brand management.",
            "items": ["Brand Identity Design", "Marketing Materials Design", "Brand Style Guide", "Social Media Management"],
            "note": "Monthly Creative Support",
            "cta": "SUBSCRIBE NOW",
            "featured": False,
        },
    ],
    "portfolio": [
        {"name": "Mango 4G Campaign", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/mango-4g.jpg"},
        {"name": "BetPawa Campaign", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/betpawa-campaign.jpg"},
        {"name": "Crypto Poster", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/crypto-top-coins.jpg"},
        {"name": "Rooted Institute Training 01", "desc": "Portfolio work added for Graphic Audition.", "image": "main/images/rooted-institute-1.jpg"},
        {"name": "Rooted Institute Training 02", "desc": "Portfolio work added for Graphic Audition.", "image": "main/images/rooted-institute-2.jpg"},
        {"name": "Nova Skills Training", "desc": "Portfolio work added for Graphic Audition.", "image": "main/images/nova-skills.jpg"},
        {"name": "Bonsoir Evening Visual", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/bonsoir-evening.jpg"},
        {"name": "Bonsoir Friday Post", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/bonsoir-friday.jpg"},
        {"name": "Creative Flyer", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/ga-creative-flyer.jpg"},
        {"name": "Beyond Limits Creative", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/beyond-limits.jpg"},
        {"name": "Cent Logo Presentation", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/cent-logo.jpg"},
        {"name": "Nova Mockup", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/nova-brand.jpg"},
    ],
    "stats": [
        {"number": "12+", "label": "Featured Projects"},
        {"number": "6+", "label": "Core Services"},
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

def _ctx(page_title, extra=None):
    ctx = dict(BASE_CONTEXT)
    ctx["page_title"] = page_title
    if extra:
        ctx.update(extra)
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
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        service = request.POST.get("service", "").strip()
        message = request.POST.get("message", "").strip()

        form_data = {
            "name": name,
            "email": email,
            "phone": phone,
            "service": service,
            "message": message,
        }

        if not all([name, email, phone, service, message]):
            return render(
                request,
                "main/contact.html",
                _ctx("Contact", {"error": "Please fill in all fields before sending.", "form_data": form_data}),
            )

        body = f"""New contact form submission

Full Name: {name}
Email: {email}
Phone / WhatsApp: {phone}
Service Needed: {service}

Project Details:
{message}
"""
        try:
            send_mail(
                subject=f"Graphic Audition Contact: {name}",
                message=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_RECEIVER_EMAIL],
                fail_silently=False,
            )
            return render(
                request,
                "main/contact.html",
                _ctx("Contact", {"success": "Your message has been sent successfully.", "form_data": {}}),
            )
        except Exception:
            return render(
                request,
                "main/contact.html",
                _ctx(
                    "Contact",
                    {
                        "error": "Email is not configured yet on Render. Add your Gmail app password in Environment and deploy again.",
                        "form_data": form_data,
                    },
                ),
            )

    return render(request, "main/contact.html", _ctx("Contact", {"form_data": {}}))
