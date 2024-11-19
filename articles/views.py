from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)

from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, FormView

from django.urls import reverse_lazy, reverse

from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .forms import CommentForm

from .models import Article

# Create your views here.


class ArticleListView(LoginRequiredMixin, ListView):
    """Articles List View"""

    model = Article
    template_name = "article_list.html"


class ArticleDetailView(LoginRequiredMixin, DetailView, FormView):
    """Artivle Detial View"""

    model = Article
    form_class = CommentForm
    template_name = "article_detail.html"

    def post(self, request, *args, **kwargs):
        """handle post request"""
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        article = self.get_object()
        return reverse("article_detail", kwargs={"pk": article.pk})


class ArticleCreateView(LoginRequiredMixin, CreateView):
    """article create view"""

    model = Article
    template_name = "article_new.html"
    fields = (
        "title",
        "body",
    )

    def form_valid(self, form):
        """return user who created the form"""
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Article update view"""

    model = Article
    fields = ("title", "body")
    template_name = "article_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Article Delete View"""

    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleLikeView(LoginRequiredMixin, View):
    """like view"""

    def get(self, request, *args, **kwargs):
        """Get Request"""

        article_id = request.GET.get("article_id", None)
        article_action = request.GET.get("article_action", None)

        print(article_id)
        print(article_action)

        article = Article.objects.get(id=article_id)

        if article_action == "like":
            # like stuff
            article.likes.add(request.user)
            article.save()
        else:
            # unlike stuff
            article.likes.remove(request.user)

        return JsonResponse(
            {
                "success": True,
            }
        )
