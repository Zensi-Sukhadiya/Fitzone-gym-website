from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('trainers/', views.trainers, name='trainers'),
    path('plans/', views.plans, name='plans'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
]

