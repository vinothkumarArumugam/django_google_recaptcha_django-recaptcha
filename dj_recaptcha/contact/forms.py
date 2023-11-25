from django import forms
from django_recaptcha.fields import ReCaptchaField 
class ContactForm(forms.Form):
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)
    captcha=ReCaptchaField()



# Create your views here.
