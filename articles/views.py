from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from django.urls import reverse_lazy

from .models import Article

# Create your views here.


class ArticleListView(ListView):
    """Articles List View"""

    model = Article
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    """Article Detial View"""

    model = Article
    template_name = "article_detail.html"


class ArticleCreateView(CreateView):
    """article create view"""

    model = Article
    template_name = "article_new.html"
    fields = ("title", "body", "author")


class ArticleUpdateView(UpdateView):
    """Article update view"""

    model = Article
    fields = ("title", "body")
    template_name = "article_edit.html"


class ArticleDeleteView(DeleteView):
    """Article Delete View"""

    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")
