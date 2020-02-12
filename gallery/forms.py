# from django.views.generic import CreateView
from django import forms
from .models import Artist, Creation

class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = ('avatar', 'name', 'year_born', 'year_died', 'bio_url',)


class CreationForm(forms.ModelForm):
#class CreationForm(CreateView): 
    class Meta:
        model = Creation
        fields = ('artist', 'title', 'year_completed', 'medium', 'image', 'artist',)