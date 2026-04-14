from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import ContactForm

BASE_CONTEXT = {
    "brand_name": "Graphic Audition",
    "phone_display": "0794 001 354",
    "phone_link": "250794001354",
    "instagram_url": "https://www.instagram.com/graphic_auditions?igsh=MXB5NjlzZmp4NzAwcw==",
    "email_display": "graphicauditions@gmail.com",
    "services": [
        {"title": "Brand Identity", "text": "Logo systems, color direction, and premium brand presentation for businesses that want to look serious."},
        {"title": "Social Media Design", "text": "Creative posts, campaign visuals, and promotional content that make your page look stronger."},
        {"title": "Flyer & Poster Design", "text": "Clean, bold flyer layouts for events, products, services, and announcements."},
        {"title": "Web Design", "text": "Modern websites that present your work professionally and help people trust your brand."},
        {"title": "Mockups & Presentation", "text": "Premium mockups and brand previews that make your design work feel polished."},
        {"title": "Campaign Visuals", "text": "Launch creatives, offer promotions, and ad-ready visuals built to attract attention."},
    ],
    "portfolio": [
        {"name": "Rooted Institute Analytics Flyer", "desc": "Training campaign design with bold typography and a premium blue visual direction.", "image": "main/images/rooted-institute-1.jpg"},
        {"name": "Rooted Institute Training Promo", "desc": "Education campaign design focused on clarity, energy, and social media engagement.", "image": "main/images/rooted-institute-2.jpg"},
        {"name": "Nova Skills Training Flyer", "desc": "Creative promotion for short-term training with a clean layout and strong call to action.", "image": "main/images/nova-skills.jpg"},
        {"name": "Mango 4G Campaign", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/mango-4g.jpg"},
        {"name": "BetPawa Campaign", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/betpawa-campaign.jpg"},
        {"name": "Crypto Poster", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/crypto-top-coins.jpg"},
        {"name": "Bonsoir Evening Visual", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/bonsoir-evening.jpg"},
        {"name": "Bonsoir Friday Post", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/bonsoir-friday.jpg"},
        {"name": "Bonsoir Table Visual", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/bonsoir-table.jpg"},
        {"name": "Bonsoir Eid Design", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/bonsoir-eid.jpg"},
        {"name": "Creative Flyer", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/ga-creative-flyer.jpg"},
        {"name": "Beyond Limits Creative", "desc": "Premium creative work by Graphic Audition.", "image": "main/images/beyond-limits.jpg"},
    ],
    "stats": [
        {"number": "20+", "label": "Creative Samples"},
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
        {
            "title": "Starter Package",
            "subtitle": "Perfect for startups & small businesses.",
            "price": "One-Time Fee",
            "items": ["Logo Design", "Brand Style Guide", "3 Social Media Templates", "Flyer or Poster Design"],
            "cta": "Get Started",
        },
        {
            "title": "Professional Package",
            "subtitle": "Comprehensive branding & digital presence.",
            "price": "Setup Fee + Monthly Subscription",
            "items": ["Brand Identity Design", "Marketing Materials", "Social Media Content", "Website Design & Development", "Website Maintenance"],
            "cta": "Get a Consultation",
        },
        {
            "title": "Essential Package",
            "subtitle": "Ongoing support for social media growth.",
            "price": "Monthly Subscription",
            "items": ["Brand Identity Support", "Marketing Material Design", "Brand Style Direction", "Monthly Social Media Management"],
            "cta": "Subscribe Now",
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
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f"New Graphic Audition inquiry from {cd['name']}"
            body = (
                f"Name: {cd['name']}\n"
                f"Email: {cd['email']}\n"
                f"Phone: {cd['phone']}\n"
                f"Service: {cd['service']}\n\n"
                f"Message:\n{cd['message']}"
            )
            try:
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.CONTACT_RECEIVER_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, "Your message has been sent successfully.")
                return redirect("contact")
            except Exception:
                messages.error(request, "Form saved, but email sending needs SMTP setup before it can deliver to Gmail.")
        else:
            messages.error(request, "Please fill in the form correctly.")
    else:
        form = ContactForm()
    ctx["form"] = form
    return render(request, "main/contact.html", ctx)
