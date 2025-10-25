from django import forms
from .models import Place

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'place_type', 'location', 'description', 'rating', 'site', 'menu', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'rating': forms.NumberInput(attrs={'min': 0, 'max': 5, 'step': 0.5}),
        }
        labels = {
            'name': 'Назва місця',
            'place_type': 'Тип місця',
            'location': 'Локація',
            'description': 'Опис',
            'rating': 'Рейтинг (0-5)',
            'site': 'Веб-сайт',
            'menu': 'Посилання на меню',
            'image': 'Зображення',
        }
