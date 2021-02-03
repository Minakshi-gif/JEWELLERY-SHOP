from django import forms  

from firstapp.models import Login
from firstapp.models import Contact

#from firstapp.models import Imagetable
from firstapp.models import Registration

class LoginForm(forms.ModelForm):  
    class Meta:  
        model = Login 
        fields = "__all__"  


class RegistarForm(forms.ModelForm):  
    class Meta:  
        model = Registration 
        fields = "__all__"  


class ContactForm(forms.ModelForm):  
    class Meta:  
          model = Contact
          fields = "__all__"  


    
    
    