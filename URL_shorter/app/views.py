import random
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import short_urls
from .forms import UrlForm
from .shortner import shortner



def LongUrlPage(request, token):

    hits = short_urls.objects.filter(short_url=token)[0]
    hits.hits = hits.hits + 1
    short_urls.save(hits)
    long_url = short_urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)

def UrlInfo(request, token):
    hits = short_urls.objects.filter(short_url=token)[0]
    long_url = short_urls.objects.filter(short_url=token)[0]
    user_index = short_urls.objects.filter(short_url=token)[0]
    u = User.objects.all()
    x= user_index.user_index
    return render(request,'app/info.html',{'user':u[x-1].username,'longurl':long_url.long_url,'hits': hits.hits,'token': token })




def Make(request):
    form = UrlForm(request.POST)
    url = ""
    text=''
    user = User.objects.all()
    if request.method == "POST":
        if form.is_valid():
            NewUrl = form.save(commit=False)
            url = shortner().issue_token()
            NewUrl.short_url = url
            NewUrl.user_index = random.randint(1,len(user))
            NewUrl.save()
            text = 'Click for mor information   !'
        else:
            form = UrlForm()
            text = "Invalid URL"

    return render(request, 'app/index.html', {'form': form, 'text': text,'url':url})
