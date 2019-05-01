from django import forms
from employee.controlModel import Employee
from parsley.decorators import parsleyfy

@parsleyfy
class RegisterUserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password must to equl to password*'}))
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
			'password': forms.PasswordInput,
            'contact': forms.NumberInput,
		}
        parsley_extras = {
            'password': {
                'minlength': "8",
                'error-message': "Your passwords at least 8 character.",
            },
            'confirm_password':{
                'equalto': "password",
                'error-message': "Confirm password do not match.",
            },
            'contact':{
                 'minlength': "10",
                'error-message': "At least 10 digit",
                },
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['full_name'].widget.attrs = {'class':'form-control', 'placeholder':'Your Full Name *'}
        self.fields['email'].widget.attrs = {'class':'form-control', 'placeholder':'Your Email Address *'}
        self.fields['contact'].widget.attrs = {'class':'form-control', 'placeholder':'Your Contact *','required':True}
        self.fields['password'].widget.attrs = {'class':'form-control', 'placeholder':'Password at least 8 Character *', 'required':True}

@parsleyfy
class LoginForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['email','password']
        widgets = {
			'password': forms.PasswordInput,
		}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs = {'class':'form-control', 'placeholder':'Your Email Address *'}
        self.fields['password'].widget.attrs = {'class':'form-control', 'placeholder':'Password at least 8 Character *'}

@parsleyfy
class AddEmployee(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
            'contact': forms.NumberInput(),
        }
        parsley_extras = {
            'contact':{
                'minlength': '10',
                'error-message': 'Enter al least 10 digit.'
            },
            'password':{
                'minlength':'8',
                'error-message': 'Password minimum 8 digit.' 
            }
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs = {'class': 'form-control col-md-7 col-xs-12','placeholder':'First Name'}
        self.fields['email'].widget.attrs = {'class':'form-control col-md-7 col-xs-12', 'placeholder':'Your Email Address *'}
        self.fields['contact'].widget.attrs = {'class':'form-control col-md-7 col-xs-12', 'placeholder':'Your Contact *'}
        self.fields['password'].widget.attrs = {'class':'form-control col-md-7 col-xs-12', 'placeholder':'Password at least 8 Character *'}

@parsleyfy  
class BulkImport(forms.ModelForm):
    import_employee = forms.FileField()
    class Meta:
        model = Employee
        fields = '__all__'



                