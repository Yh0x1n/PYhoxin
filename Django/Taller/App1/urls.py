from django.urls import path
from .views import indexView, autorView

urlpatterns = [
    path('', indexView),
    path('autor/<int:id>', autorView)
]