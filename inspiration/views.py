from django.shortcuts import render

# Create your views here.
def poem_list(request):
    return render(request, 'inspiration/poem_list.html', {})