from django.forms import ModelForm
from django import forms
from .models import AnnouncementModel, GlobalSettingsModel


# class AnnouncementsCountForm(forms.Form):
#     choices = [(str(x), x) for x in range(1, 9)]
#     value = forms.ChoiceField(choices=choices)

class AnnouncementsCountForm(ModelForm):
    class Meta:
        model = GlobalSettingsModel
        fields = ['value']
        choices = [(str(x), x) for x in range(1, 9)]
        widgets = {
            'value': forms.Select(choices=choices, attrs={'onchange': 'submit()'})
        }
        labels = {
            'value': 'Number of announcements'
        }


class AnnouncementForm(ModelForm):
    class Meta:
        model = AnnouncementModel
        fields = ['cs', 'en', 'de']  # '__all__'
        widgets = {
            'cs': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'en': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'de': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
