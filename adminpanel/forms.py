from django import forms
from events.models import Event


class EventForm(forms.ModelForm):

    class Meta:

        model = Event

        fields = [
            "title",
            "venue",
            "date",
            "description",
            "image",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Event Title"
                }
            ),

            "venue": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Venue"
                }
            ),

            "date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Enter Event Description"
                }
            ),

            "image": forms.FileInput(
                attrs={
                    "class": "form-control"
                }
            ),

        }
