# encoding: utf-8
# @author: John
# @contact: BoHongtao@yeah.net
# @software: PyCharm
# @time: 2018/7/6 10:48
from django.http import HttpResponse
from django.shortcuts import render
def Hello(request):
    # return HttpResponse('Hello Django')
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)