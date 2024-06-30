from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("<slug:slug>", views.book_detail, name="book_detail"), 
    path("bestsellers", views.bestsellers, name="bestsellers")
]