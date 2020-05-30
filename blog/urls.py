from django.contrib import admin
from django.urls import path

from .views import *

app_name = 'blog'

urlpatterns = [
    path('',BlogDetails,name='home'),
    path('detail/<int:blog_id>/',detail,name='detail'),
    path('blogs/all',whole_blog,name='all')
]