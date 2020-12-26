from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    context = {
        'title':'Hello world'
    }
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        context['premium_content']='YEAHHHH'
    return render(request, 'home_page.html', context)

def about_page(request):
    context = {
        'title':'About Page'
    }
    return render(request, 'about_page.html', context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'form': contact_form,
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # if request.method == 'POST':
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))

    return render(request, 'contact_page.html', context)


def login_page(request):

    login_form = LoginForm(request.POST or None)
    context = {
        'form': login_form,
    }

    print(request.user)
    print(request.user.is_authenticated)

    if login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # context['form'] = LoginForm()
            return redirect('/')
        else:
            print('Error')
    return render(request, 'auth/login.html', context)

User = get_user_model()
def register_page(request):
    register_form = RegisterForm(request.POST or None)
    context = {
        'form': register_form,
    }
    if register_form.is_valid():

        username = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        password2 = register_form.cleaned_data.get('password2')
        print(register_form.cleaned_data)
        new_user = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, 'auth/register.html', context)