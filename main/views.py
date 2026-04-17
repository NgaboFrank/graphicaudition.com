from django.shortcuts import render

BASE_CONTEXT = {
    "brand_name": "Graphic Audition",
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
        {"name": "Bonsoir Women’s Day Campaign", "desc": "Social campaign creative designed for Bonsoir.", "image": "main/images/bonsoir-womens-day.jpg"},
        {"name": "Bonsoir Eid Mubarak Visual", "desc": "Festive promotional design for the Bonsoir brand.", "image": "main/images/bonsoir-eid-new.jpg"},
        {"name": "Bonsoir Lifestyle Campaign", "desc": "Brand storytelling visual created for Bonsoir.", "image": "main/images/bonsoir-stressfree.jpg"},
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
        {"name": "Rooted Institute Data Analytics Training", "desc": "Training campaign creative for The Rooted Institute.", "image": "main/images/rooted-institute-training-1.jpg"},
        {"name": "Rooted Institute Team Training Visual", "desc": "Promotional training visual showing a collaborative learning environment.", "image": "main/images/rooted-institute-training-2.jpg"},
        {"name": "Nova Mobile Brand Mockup", "desc": "Clean mobile mockup presentation for the Nova brand.", "image": "main/images/nova-phone.jpg"},
        {"name": "Nova Skills Training Campaign", "desc": "Training campaign flyer created for Nova Skills.", "image": "main/images/nova-skills-training.jpg"},
        {"name": "Bonsoir Sit & Relax Campaign", "desc": "Bonsoir promotional visual focused on premium event and evening branding.", "image": "main/images/bonsoir-sit-relax.jpg"},
        {"name": "Bonsoir Why Us Campaign", "desc": "Brand communication visual created for Bonsoir.", "image": "main/images/bonsoir-why-us.jpg"},
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
    return render(request, "main/contact.html", _ctx("Contact"))
