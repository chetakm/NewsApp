from django.shortcuts import render,HttpResponse
import requests
# Create your views here.
def index(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=8004042b28617f241595db46f95a96fd&countries=es')
    res = r.json()
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])
    news = zip(title,description,image,url)
    return render(request,'newsapp/index.html',{'news':news})