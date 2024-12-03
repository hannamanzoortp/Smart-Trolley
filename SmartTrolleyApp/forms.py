from django.forms import ModelForm

from SmartTrolleyApp.models import *


class StaffForm(ModelForm):
    class Meta:
        model = StaffTable
        fields = ['Name','Age','Area','PhoneNumber','Qualification','Salary','Address']

class LoginForm(ModelForm):
    class Meta:
        model = LoginTable
        fields = ['Username','Password','Type']

class ProductForm(ModelForm):
    class Meta:
        model = ProductTable
        fields = ['Image','Name','Price','ManufacturingDate','ExpiryDate','BrandName']
        

        

        
