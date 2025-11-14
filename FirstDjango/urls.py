from django.urls import path, re_path
from MainApp import views


urlpatterns = [
    path("", views.home),
    path("about/", views.about, name="about"),
    path("item/<int:id>/", views.get_item, name="item-detail"),
    path("items/", views.get_all_items, name="all_items"),
]
