from django.conf.urls import url
from mysite import views

urlpatterns = [
    url(r'^$',views.Home,name='home-page'),
    url(r'^get/',views.Details,name='details')
]