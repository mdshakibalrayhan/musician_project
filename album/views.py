from django.shortcuts import render,redirect
from .forms import AlbumForm
from .models import Album
from music_owner.models import Musician
from music_owner.forms import MusicianForm
# Create your views here.
def add_album(request):
    if request.method == 'POST':
        add_album = AlbumForm(request.POST)
        if add_album.is_valid():
            add_album.save()
            return redirect('add_album')
        else:
            print(add_album.errors)
    else:
        add_album = AlbumForm()
    return render(request,'album.html',{'form':add_album})


def edit_data(request,id):
    data = Album.objects.get(pk = id)
    form = AlbumForm(instance=data)
    if request.method == 'POST':
        form = AlbumForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request,'album.html',{'form':form})

def edit_musician(request,id):
    data = Musician.objects.get(pk = id)
    form = MusicianForm(instance=data)
    if request.method == 'POST':
        form = MusicianForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request,'musician.html',{'form':form})


def delete_data(request,id):
    data = Album.objects.get(pk = id)
    data.delete()
    return redirect('homepage')