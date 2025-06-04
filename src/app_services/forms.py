from django import forms
from .models import Service


class ServicesForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price', 'active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            else:
                field.widget.attrs.update(
                    {'class': 'form-control form-control-lg'})
