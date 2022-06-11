from django import forms


class CityForm(forms.Form):
    city = forms.CharField(label='City Name', max_length=25, required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'City name'})
                           )
