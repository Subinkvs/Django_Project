from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
import re


class CustomUserCreation(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter confirmpassword'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter phonenumber'}))
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        
        if not username.isalnum():
            raise forms.ValidationError("Username should not consists numbers")
        
        if len(username) <= 3:
            raise forms.ValidationError("Given username is too short")
        
        return username
    
    def clean_email(self):
            email = self.cleaned_data.get('email')
            char = '@'
            position = email.find(char)
    
    
            if char not in email:
                raise forms.ValidationError("Invalid address..")
        
            if position < 3:
                raise forms.ValidationError("Sorry, your email address is too short")
    

            if CustomUser.objects.filter(email=email).exists():
                raise forms.ValidationError("Given email address already exists.")
    
    
            return email
        
    def clean_phone_number(self):
        phone_number = self.cleaned_data('phone_number')
        
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("Given number is already exists")
        
        if not re.match(r'^\+91[0-9]{10}$', phone_number):
            raise forms.ValidationError('Phone number is not in standard format...Please try again!')
        
        return phone_number
            
       
            
        
                
            