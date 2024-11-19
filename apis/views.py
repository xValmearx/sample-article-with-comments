from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View

from articles.models import Article, Comment


class ApiCommentDetailView(LoginRequiredMixin, View):
    """detail of comment returned as JSON"""

    def get(self, request, article_pk, comment_pk, *args, **kwargs):
        comment = Comment.objects.values().get(
            pk=comment_pk,
        )
        return JsonResponse(comment, safe=False)


class ApiCommentListView(LoginRequiredMixin, View):
    """List of Comments for an Article returned as JSON"""

    def get(self, reqest, article_pk, *args, **kwargs):
        """Get Request"""
        comments = list(
            Comment.objects.filter(
                article__pk=article_pk,
            ).values()
        )

        return JsonResponse(comments, safe=False)


class ApiArticleDetailView(LoginRequiredMixin, View):
    """Detail of Article returned as JSON"""

    def get(self, request, article_pk, *args, **kwargs):
        article = Article.objects.values().get(pk=article_pk)

        return JsonResponse(article, safe=False)


class ApiArticleListView(LoginRequiredMixin, View):
    """List of Articles returned as JSON"""

    def get(self, request, *args, **kwargs):
        """get request"""
        articles = list(Article.objects.values())
        return JsonResponse(articles, safe=False)
