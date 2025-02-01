from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='home'),
    path('post/<int:id>/',views.detail,name='detail'),
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout')
]