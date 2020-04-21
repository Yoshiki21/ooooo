from django.urls import path

from . import views

app_name = 'ECT'
urlpatterns = [
    path('edit/<int:num>/', views.edit, name = 'edit'),
    path('create/', views.create, name = 'create'),
    path('<int:meeting_id>/', views.detail, name = 'detail'),
    path('', views.index, name='index'),
]