from django import  forms

class LifeForm(forms.Form):
    lifeName = forms.CharField()
    lifeText = forms.TextInput()
    picture = forms.ImageField()