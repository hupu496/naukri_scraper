from django import forms

from django import forms

class ScrapeForm(forms.Form):
    PLATFORM_CHOICES = [('naukri', 'Naukri Resdex'), ('linkedin', 'LinkedIn')]

    platform = forms.ChoiceField(choices=PLATFORM_CHOICES)

    keywords = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Python Developer, Data Scientist'}),
        help_text="Skills / Keywords (Required)"
    )

    education = forms.CharField(required=False,
        widget=forms.TextInput(attrs={'placeholder': 'B.Tech, MBA, IIT'}),
        help_text="Education")

    location = forms.CharField(required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Bangalore, Delhi, Remote'}),
        help_text="Location")

    max_items = forms.IntegerField(initial=20, min_value=5, max_value=100)