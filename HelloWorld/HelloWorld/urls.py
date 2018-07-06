from django.conf.urls import url
from . import view,getall

urlpatterns = [
    url(r'^$', view.Hello),
    url(r'^tmall$', getall.getall),
]
