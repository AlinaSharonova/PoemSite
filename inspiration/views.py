from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Poem
from .forms import PoemForm
from django.shortcuts import redirect

# Create your views here.
def poem_list(request):
    poems = Poem.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'inspiration/poem_list.html', {'poems': poems})


def poem_detail(request, pk):
    poem = get_object_or_404(Poem, pk=pk)
    return render(request, 'inspiration/poem_detail.html', {'poem': poem})

def poem_new(request):
    if request.method == "POST":
        form = PoemForm(request.POST)
        if form.is_valid():
            poem = form.save(commit=False)
            poem.author = request.user
            poem.published_date = timezone.now()
            poem.save()
            return redirect('poem_detail', pk=poem.pk)
    else:
        form = PoemForm()
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