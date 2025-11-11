from django.urls import path, re_path
from MainApp import views


urlpatterns = [
    path("", views.home),
    path("about/", views.about),
    re_path(r"^item/(?P<id>[1-9]|10)/$", views.get_items),
]
