from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
import urllib.request, urllib.error, urllib.parse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
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
    # else:
    #         print("hello")
    #         urlob = request.POST.get('url')
    #         # urres = request.get('url').status_code
    #         # urres = HttpResponse(urlob).status_code
    #         response = urllib.request.urlopen(urlob)
    #         webContent = response.read()
    #         urres = webContent
    #         urlmod = urlMod(basicurl = urlob,
    #                         basiccontent = urres
    #         );
    #         # urlmod.save()
    #         # print(webContent)
    #         # return redirect(urlob)
    #         context={}
    #         context['response']=webContent
    #         print(context['response'])
    #
    #         return render(request,'urlcontent.html',context)



def display(request):
    # print("hello")
    urlob = request.POST.get('url')
    try:
        response = urllib.request.urlopen(urlob)
    except:
        return redirect('index')
    webContent = response.read()
    encoding = response.headers.get_content_charset('utf-8')
    html_text = webContent.decode(encoding)

    urres = html_text

    urlmod = urlMod(basicurl=urlob,
                    basiccontent=urres
                    );
    try:
        urlmod.save()
    except:
        pass
    # print(webContent)
    return render(request,'urlcontent.html', { 'response' : html_text })

