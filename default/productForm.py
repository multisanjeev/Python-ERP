from django import forms
from parsley.decorators import parsleyfy
from .models import Product

@parsleyfy
class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'specification': forms.Textarea()
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {'class':'form-control'}
        self.fields['description'].widget.attrs = {'class':'form-control'}
        self.fields['specification'].widget.attrs = {'class':'form-control'}
        self.fields['specification'].required = False
        self.fields['category'].widget.attrs = {'class': 'form-control'}

class ImportProduct(forms.ModelForm):
    import_product = forms.FileField()
    class Meta:
        model = Product
        fields = '__all__'
