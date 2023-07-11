from django.urls import path
from crm import views

app_name = 'crm'
urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('c60/', views.C60sListView.as_view(), name='common60'),
]
