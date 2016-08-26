from django.conf.urls import  url

from HelloWorld import views

urlpatterns=[

    url(r'^',views.hello,name='hello')
]