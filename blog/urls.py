from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('posts/', views.posts, name='posts'),
    path('post/<int:id>/', views.post, name='post'),
    path('post/<slug:slug>/', views.post, name='post'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('send_email/', views.sendEmail, name = 'send_email'),
]