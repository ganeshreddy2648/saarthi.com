from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
# Create your views here.
from urlink.models import urlMod


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password=password)
            login(request, user)
            return redirect('index')
    else:
            form = UserCreationForm()
    context = {'form':form}
    return render(request,'registration/register.html',context)

def index(request):
    if request.method == 'GET':
        return render(request,'index.html')
    else:
            urlob = request.POST.get('url')
            urres = request.get('url').status_code

            urlmod = urlMod(basicurl = urlob,
                            basiccontent = urres
            );
            urlmod.save()
            return render(request,urlob)






