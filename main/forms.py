from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={"placeholder": "Your full name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Your email address"}))
    phone = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={"placeholder": "Your phone number"}))
    service = forms.CharField(max_length=120, required=False, widget=forms.TextInput(attrs={"placeholder": "Service you need"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Tell us about your project", "rows": 6}))
