from django import forms

SERVICE_CHOICES = [
    ("Brand Identity", "Brand Identity"),
    ("Social Media Design", "Social Media Design"),
    ("Flyer & Poster Design", "Flyer & Poster Design"),
    ("Website Design", "Website Design"),
    ("Mockups & Presentation", "Mockups & Presentation"),
    ("Other", "Other"),
]


class ContactForm(forms.Form):
    name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={"placeholder": "Your full name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Your email address"}))
    phone = forms.CharField(max_length=40, required=False, widget=forms.TextInput(attrs={"placeholder": "Phone / WhatsApp"}))
    service = forms.ChoiceField(choices=SERVICE_CHOICES)
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Tell us about your project", "rows": 6}))
