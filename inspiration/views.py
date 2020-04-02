from django.shortcuts import render
from django.utils import timezone
from .models import Poem

# Create your views here.
def poem_list(request):
    poems = Poem.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'inspiration/poem_list.html', {'poems': poems})
