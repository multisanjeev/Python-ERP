from django import forms
from parsley.decorators import parsleyfy
from .models import Categories

@parsleyfy
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {'class':'form-control'}
        self.fields['description'].widget.attrs = {'class':'form-control'}
        self.fields['display_order'].widget.attrs = {'class':'form-control'}

@parsleyfy  
class ImportCategory(forms.ModelForm):
    import_category = forms.FileField()
    class Meta:
        model = Categories
        fields = '__all__'