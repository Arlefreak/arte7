from django import forms

CONTACT_CHOICES = (
    ('CAR', 'carrera de cine'),
    ('WOR', 'workshop de realización cinematográfica'),
    ('DIP', 'diplomado en realización cinematográfica'),
    ('VER', 'workshop de verano'),
    ('OTR', 'otros'),
)

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    contact_phone = forms.CharField(required=True)
    contact_interest = forms.ChoiceField(choices=CONTACT_CHOICES, required=True)
    contact_message = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
