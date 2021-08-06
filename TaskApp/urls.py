from django.urls import path
from .views import index,post,get,edit
urlpatterns = [
    path('',index,name='index'),
    path('post/',post,name='post'),
    path('<str:link>/',get,name='get'),
    path('edit/<str:link>/',edit,name='edit'),
]
