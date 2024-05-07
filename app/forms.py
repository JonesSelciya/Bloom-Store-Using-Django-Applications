from django import forms
from .models import bloom

class myform(forms.ModelForm):
    class Meta:
        model = bloom  # Replace YourModel with the name of your model
        fields = '__all__'

# class add(forms.Modelform):
#     class Meta:
#         model= addtocart
#         fields = '__all__'
