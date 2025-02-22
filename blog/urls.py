from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='home'),
    path('post/<int:id>/',views.detail,name='detail'),
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('create_post/',views.create_post,name='create_post'),
    path('update_post/<int:id>/',views.update_post,name='update_post'),
]