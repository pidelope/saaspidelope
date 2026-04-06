from django.urls import path
from . import views

app_name = 'business'

urlpatterns = [
    path('p/<slug:business_slug>/<str:table_number>/', views.public_menu, name='public_menu'),
]
