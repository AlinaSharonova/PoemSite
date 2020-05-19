from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Poem
from .forms import PoemForm
#UserEditForm, ProfileEditForm, UserRegistrationForm  oemFilterForm
from django.shortcuts import redirect

# Create your views here. Переделать на классы

# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             # Create a new user object but avoid saving it yet
#             new_user = user_form.save(commit=False)
#             # Set the chosen password
#             new_user.set_password(user_form.cleaned_data['password'])
#             # Save the User object
#             new_user.save()
#             profile = Profile.objects.create(user=new_user)
#             return render(request, 'registration/register_done.html', {'new_user': new_user})
#     else:
#         user_form = UserRegistrationForm()
#     return render(request, 'registration/register.html', {'user_form': user_form})
#
# @login_required
# def edit(request):
#     if request.method == 'POST':
#         user_form = UserEditForm(instance=request.user, data=request.POST)
#         profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#     else:
#         user_form = UserEditForm(instance=request.user)
#         profile_form = ProfileEditForm(instance=request.user.profile)
#         return render(request,
#                       'inspiration/edit_profile.html',
#                       {'user_form': user_form,
#                        'profile_form': profile_form})

def poem_list(request):
    poems = Poem.objects.all()

    # Фильтрация для пользователя
    #form = PoemFilterForm(request.GET)

    # if form.is_valid():
    #     if form.cleaned_data["ordering"]:
    #         poems = poems.order_by(form.cleaned_data["ordering"])

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