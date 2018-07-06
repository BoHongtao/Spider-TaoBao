# encoding: utf-8
# @author: John
# @contact: BoHongtao@yeah.net
# @software: PyCharm
# @time: 2018/7/6 13:07

from django.http import HttpResponse
from Tmall.models import Tmall
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

def getall(request):
    # 初始化
    response = ""
    response1 = ""
    listall = Tmall.objects.all()
    paginator = Paginator(listall, 25)
    page = request.GET.get('page')
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        list = paginator.page(paginator.num_pages)
    return render(request, 'list.html', {'list':list})
