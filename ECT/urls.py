from django.urls import path

from . import views

app_name = 'ECT'
urlpatterns = [
    path('<int:meeting_id>/', views.detail, name = 'detail'),
    path('', views.index, name='index'),
]