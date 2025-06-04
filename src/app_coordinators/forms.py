from django import forms
from .models import Coordinator


class CoordinatorsForm(forms.ModelForm):
    class Meta:
        model = Coordinator
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            else:
                field.widget.attrs.update(
                    {'class': 'form-control form-control-lg'})
