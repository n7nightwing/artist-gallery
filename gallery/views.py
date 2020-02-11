from django.shortcuts import render, redirect

from .models import Artist, Creation
from .forms import ArtistForm, CreationForm



def home(request):
    return render(request, 'gallery/home.html')


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'gallery/artist_list.html', {'artists': artists})


def artist_detail(request, pk):
    artist = Artist.objects.get(id=pk)
    return render(request, 'gallery/artist_detail.html', {'artist': artist})


def artist_create(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm()
    return render(request, 'gallery/artist_form.html', {'form': form})


def artist_edit(request, pk):
    artist = Artist.objects.get(pk=pk)
    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'gallery/artist_form.html', {'form': form})


def artist_delete(request, pk):
    Artist.objects.get(id=pk).delete()
    return redirect('artist_list')


def creation_list(request):
    creations = Creation.objects.all()
    return render(request, 'gallery/creation_list.html', {'creations': creations})


def creation_detail(request, pk):
    creation = Creation.objects.get(id=pk)
    return render(request, 'gallery/creation_detail.html', {'creation': creation})


def creation_create(request):
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            creation = form.save()
            return redirect('creation_detail', pk=creation.pk)
    else:
        form = CreationForm()
    return render(request, 'gallery/creation_form.html', {'form': form})


def creation_edit(request, pk):
    creation = Creation.objects.get(pk=pk)
    if request.method == "POST":
        form = CreationForm(request.POST, instance=creation)
        if form.is_valid():
            artist = form.save()
            return redirect('creation_detail', pk=creation.pk)
    else:
        form = CreationForm(instance=creation)
    return render(request, 'gallery/creation_form.html', {'form': form})


def creation_delete(request, pk):
    Creation.objects.get(id=pk).delete()
    return redirect('creation_list')