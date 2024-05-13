from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name='home'),
    path("text_entry/", views.text_entry, name="text_entry"),
    path("get_link/", views.get_link, name="get_link"),
    path("get_text/", views.get_text, name="get_text"),
]