from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from .models import Post
import json
def index(request):
    return render(request,'index.html',{})
def post(request):
    try:
        data = json.loads(request.body)
        if data['id']!=0:
            p = Post.objects.get(id=data['id'])
            p.title = data['title']
            p.name = data['name']
            p.text = data['text']
        else:
            p = Post.objects.create(
                title=data['title'],
                name=data['name'],
                text=data['text']
            )
        p.save()
        return JsonResponse({'url':f'''https://{get_current_site(request)}/{p.title}-{p.date}'''},status=200)
    except Exception as e:
        return JsonResponse({'error':e},status=500)
def get(request,link):
    parts = link.split('-')
    t = '-'.join(parts[:len(parts)-3])
    d = '-'.join(parts[len(parts)-3:])
    try:
        p = Post.objects.get(title=t,date=d)
        return render(request,'get.html',{'post':p,'text':p.text,'link':link})
    except Exception as e:
        return HttpResponse('<h2>404</h2>')

def edit(request,link):
    parts = link.split('-')
    t = '-'.join(parts[:len(parts)-3])
    d = '-'.join(parts[len(parts)-3:])
    try:
        p = Post.objects.get(title=t,date=d)
        return render(request,'edit.html',{'post':p,'text':p.text})
    except Exception as e:
        return HttpResponse('<h2>500</h2>')
