from django import forms

from app.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'foreign_id',
            'location_from',
            'location_to',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
