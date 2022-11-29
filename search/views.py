from django.http import HttpResponse
from django.shortcuts import render
from .models import Jobs

def index(request):
    return render(request, 'static/base.html')

def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query: #query, 검색어가 있을 시
            sector = Jobs.objects.filter(name__contains=query)
            return render(request, 'searchbar.html', {'sector': sector})
        else: #없을 시
            print("No infomation to show")
            return request(request, 'searchbar.html', {})