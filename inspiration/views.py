from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Poem

# Create your views here.
def poem_list(request):
    poems = Poem.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'inspiration/poem_list.html', {'poems': poems})


def poem_detail(request, pk):
    poem = get_object_or_404(Poem, pk=pk)
    return render(request, 'inspiration/poem_detail.html', {'poem': poem})