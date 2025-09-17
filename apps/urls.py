from django.urls import path
from . import views

app_name = "apps"

urlpatterns = [
    path("", views.home, name="home"),
    path("suggest/", views.suggest_apps, name="suggest_apps"),
    path("search/", views.search_results, name="search_results"),
    path("app/<int:app_id>/", views.app_detail, name="app_detail"),
    path("app/<int:app_id>/add_review/", views.add_review, name="add_review"),
]
