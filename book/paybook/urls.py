from django.urls import path
from . import views

app_name='paybook'


urlpatterns=[

    path('',views.book_list,name='book_list'),
]