from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='home'),
    path('post/<int:id>/',views.detail,name='detail')
]