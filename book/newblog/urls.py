from django.urls import path
from . import views

app_name='newblog'


urlpatterns=[

    path('',views.post_list,name='post_list'),
    path('formy/', views.share, name='share'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]