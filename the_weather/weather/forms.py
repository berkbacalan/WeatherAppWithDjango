from django.forms import TextInput,ModelForm


class CityForm(TextInput):
    class Meta:
        fields = ['name']
        widgets = {'name':TextInput(attrs={'class':'input', 'placeholder':'City Name'})}