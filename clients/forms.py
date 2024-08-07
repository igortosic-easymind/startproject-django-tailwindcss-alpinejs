from django import forms

from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ["created_at"]  # Exclude the 'description' field
        fields = "__all__"
