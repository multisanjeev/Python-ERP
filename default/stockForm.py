from django import forms
from .models import Stock
from parsley.decorators import parsleyfy

class AddStock(forms.ModelForm):
    current_stock = forms.CharField(widget = forms.TextInput(attrs = {'class':'form-control', 'disabled': True}))
    class Meta:
        model = Stock
        fields = ['product','new_stock']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].widget.attrs = {'class':'form-control'}
       # self.fields['current_stock'].widget.attrs = {'class':'form-control', 'disabled': True}
        self.fields['new_stock'].widget.attrs = {'class':'form-control'}