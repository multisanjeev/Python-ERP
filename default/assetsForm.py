from django import forms
from .models import Order
from parsley.decorators import parsleyfy

@parsleyfy

class CreateOrder(forms.ModelForm):
    current_stock = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control','readonly':True}))
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            "remark": forms.Textarea(),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employee'].widget.attrs = {'class': 'form-control'}
        self.fields['category'].widget.attrs = {'class': 'form-control'}
        self.fields['product'].widget.attrs = {'class': 'form-control'}
        self.fields['qty'].widget.attrs = {'class': 'form-control'}
        self.fields['remark'].widget.attrs = {'class': 'form-control'}
        self.fields['remark'].required = False
        self.fields["current_stock"].required = False
