from django import forms
from .models import Clients


class ClientsForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['first_name', 'last_name', 'email', 'phone', 'active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            else:
                field.widget.attrs.update(
                    {'class': 'form-control form-control-lg'})
