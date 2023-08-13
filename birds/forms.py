from django import forms

from .models import BirdModel, AddBirdModel


class BirdForm(forms.ModelForm):
    name = forms.CharField(label='Название птицы', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = BirdModel
        fields = ['name', 'image']


class AddBirdForm(forms.ModelForm):
    bird = forms.ModelChoiceField(queryset=BirdModel.objects.all(), label='Вид птицы',
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(label='Количество', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    city = forms.CharField(label='Город', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    region = forms.CharField(label='Регион', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    street = forms.CharField(label='Улица', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = AddBirdModel
        fields = ['bird', 'quantity', 'city', 'region', 'street']