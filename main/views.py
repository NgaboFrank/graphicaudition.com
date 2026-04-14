from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render

from .forms import ContactForm

BASE_CONTEXT = {
    "brand_name": "Graphic Audition",
    "contact_email": "graphicaudition@gmail.com",
    "phone_display": "0784 330 484",
    "phone_link": "250784330484",
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
        {"name": "Rooted Institute Project 1", "desc": "Portfolio work added for Graphic Audition.", "image": "main/images/rooted-institute-1.jpg"},
        {"name": "Rooted Institute Project 2", "desc": "Portfolio work added for Graphic Audition.", "image": "main/images/rooted-institute-2.jpg"},
        {"name": "Nova Skills Project", "desc": "Portfolio work added for Graphic Audition.", "image": "main/images/nova-skills.jpg"},
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
    "testimonials": [
        {"name": "Client Review", "text": "Excellent work from concept to final delivery. The design quality felt premium and the communication stayed clear."},
        {"name": "Business Owner", "text": "Our business looked more professional immediately. The final visuals gave us a stronger first impression."},
        {"name": "Marketing Client", "text": "The work was clean, modern, and ready to use. It matched the brand direction perfectly."},
    ],
    "packages": [
        {"name": "Starter Package", "tagline": "Perfect for startups and growing pages.", "items": ["Social media design support", "Flyers and simple promo graphics", "Clean and fast creative delivery"], "cta": "GET STARTED", "cta_note": "A simple starting point for brands that need consistent visuals."},
        {"name": "Professional Package", "tagline": "Comprehensive design support for active businesses.", "items": ["Campaign visuals and branded content", "Marketing materials and digital creatives", "Stronger presentation across platforms"], "cta": "BOOK A CONSULTATION", "cta_note": "Best for brands that want a more complete and structured visual system."},
        {"name": "Essential Package", "tagline": "Ongoing creative support for regular brand communication.", "items": ["Monthly design assistance", "Consistent brand look across content", "Reliable support for new promotions"], "cta": "CONTACT US", "cta_note": "A flexible package for businesses that need steady design work."},
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
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            receiver = getattr(settings, "CONTACT_RECEIVER_EMAIL", BASE_CONTEXT["contact_email"])
            body = (
                f"New Graphic Audition contact form submission\n\n"
                f"Name: {data['name']}\n"
                f"Email: {data['email']}\n"
                f"Phone: {data['phone'] or '-'}\n"
                f"Service: {data['service']}\n\n"
                f"Message:\n{data['message']}\n"
            )
            email = EmailMessage(
                subject=f"New website inquiry from {data['name']}",
                body=body,
                from_email=getattr(settings, "DEFAULT_FROM_EMAIL", BASE_CONTEXT["contact_email"]),
                to=[receiver],
                reply_to=[data["email"]],
            )
            try:
                email.send(fail_silently=False)
                messages.success(request, "Your message was sent successfully. We will get back to you soon.")
                return redirect("contact")
            except Exception:
                messages.error(request, "Email is not configured yet. Add your Gmail App Password in Render Environment, then try again.")
        else:
            messages.error(request, "Please correct the form and try again.")
    else:
        form = ContactForm()
    ctx["form"] = form
    return render(request, "main/contact.html", ctx)
