from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.http import HttpResponse

from django.views.generic import ListView, DetailView, UpdateView, DeleteView, FormView

from django.views.generic.detail import SingleObjectMixin

from django.urls import reverse_lazy, reverse

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views import View

from .forms import CommentForm

from .models import Article

# Create your views here.


class ArticleListView(LoginRequiredMixin, ListView):
    """Articles List View"""

    model = Article
    template_name = "article_list.html"


class ArticleDetailView(LoginRequiredMixin, View):
    """Article Detial View"""

    def get(self, request, *args, **kwargs):
        """Get Request"""
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Post Request"""
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class CommentGet(LoginRequiredMixin, DetailView):
    """Article Detial View / Add Comment Form"""

    model = Article
    template_name = "article_detail.html"

    def get_context_data(self, **kwargs):
        """Get contex data"""
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):
    """Comment Post"""

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
