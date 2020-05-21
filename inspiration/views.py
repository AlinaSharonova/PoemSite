from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from mongoengine import Q

from inspiration.forms import CommentPoemForm, PoemForm
from .models import Poem, CommentPoem

#UserEditForm, ProfileEditForm, UserRegistrationForm  oemFilterForm
from django.shortcuts import redirect



def poem_list(request):
    poems = Poem.objects.all().order_by('-published_date')
    return render(request, 'inspiration/poem_list.html', {'poems': poems})


def poem_detail(request, pk):
    poem = get_object_or_404(Poem, pk=pk)
    comment = CommentPoem.objects.filter(id_poem=pk)
    if request.method == "POST":
        form = CommentPoemForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.id_poem = poem
            form.save()
            return redirect(poem_detail, pk)
    else:
        form = CommentPoemForm()
    return render(request, 'inspiration/poem_detail.html', {'poem': poem, 'comments': comment, 'form': form})

def poem_new(request):
    form = PoemForm(request.POST or None)
    if request.method == "POST":
        #form = PoemForm(request.POST)
        if form.is_valid():
            poem = form.save(commit=False)
            poem.owner = request.user
            poem.published_date = timezone.now()
            poem.save()
            return redirect('poem', pk=poem.pk)
   # else:
        #form = PoemForm()
    return render(request, 'inspiration/poem_edit.html', {'form': form})

def poem_edit(request, pk):
    poem = get_object_or_404(Poem, pk=pk)
    if request.method == "POST":
        form = PoemForm(request.POST, instance=poem)
        if form.is_valid():
            poem = form.save(commit=False)
            poem.author = request.user
            poem.published_date = timezone.now()
            poem.save()
            return redirect('poem_detail', pk=poem.pk)
    else:
        form = PoemForm(instance=poem)
    return render(request, 'inspiration/poem_edit.html', {'form': form})

def poem_lovesad(request):
    poems = Poem.objects.filter(Q(Poem.category == 'LOVE') | Q(Poem.category == 'SAD')).order_by('-published_date')
    return render(request, 'inspiration/poem_lovesad.html', {'poems': poems})



def comment(request):
    form = CommentPoemForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.created = timezone.now()
            comment.save()
            return redirect('poem', pk=comment.pk)
    return render(request, 'inspiration/poem_edit.html', {'form': form})