from django.forms import ModelForm
from .models import *
from captcha.fields import CaptchaField

class ApplicationForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Divorce
        exclude = ['sno']
    