from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Name")
    email = forms.EmailField(required=True, label="Email")
    message = forms.CharField(
        widget=forms.Textarea,
        max_length=500,
        required=True,
        label="Message"
    )
