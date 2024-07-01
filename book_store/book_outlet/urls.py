from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("bestsellers", views.bestsellers, name="bestsellers"),
    path("<slug:slug>", views.book_detail, name="book_detail")
]