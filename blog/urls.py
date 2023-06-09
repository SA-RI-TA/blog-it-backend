from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.posts, name="posts"),
    path("<int:post_id>/", views.detail, name="detail"),
    path("<int:post_id>/results/", views.results, name="results"),
    path("<int:post_id>/vote/", views.vote, name="vote"),
]
