from django.urls import path, re_path
from MainApp import views


urlpatterns = [
    path("", views.home),
    path("about/", views.about),
    #re_path(r"^item/(?P<id>[1-9]|10)/$", views.get_items),
    path("item/<int:id>/", views.get_item),
    path("items/", views.get_all_items),
]
