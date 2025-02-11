from django.urls import path

from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleCreateView,
    ArticleLikeView,
)

urlpatterns = [
    path("<int:pk>/like/", ArticleLikeView.as_view(), name="article_like"),
    path("<int:pk>/update/", ArticleUpdateView.as_view(), name="article_edit"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    path("<int:pk>", ArticleDetailView.as_view(), name="article_detail"),
    path("new/", ArticleCreateView.as_view(), name="article_new"),
    path("", ArticleListView.as_view(), name="article_list"),
]
