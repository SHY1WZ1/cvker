from django import forms

from cvkerapp.models import CV


class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['name', 'surname', 'email', 'phone', 'photo', 'localization', 'summary', 'job_opportunity']