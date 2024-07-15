from django import forms


class FilterYtForm(forms.Form):
    date1 = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date2 = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))