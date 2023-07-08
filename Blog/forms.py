from django import forms

from Blog.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'})
        }
        
        help_texts = {'username' : ''}
        
        
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'})
        }
        
        labels = {
            'username':'Enter Username',
            'password':'Enter Password'
        }
        
        help_texts = {'username' : ''}
        

        
class ShoeForm(forms.ModelForm):
    class Meta:
        model = Shoe
        fields = '__all__'
        
        widgets = {
            'brand_name' : forms.TextInput(attrs={'class':'form-control'}),
            'shoe_name' : forms.TextInput(attrs={'class':'form-control'}),
            'shoe_image' : forms.FileInput(attrs={'class':'form-control'}),
            'price' : forms.NumberInput(attrs={'class':'form-control'}),
            'website' : forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control','rows':3, 'cols':20})
        }