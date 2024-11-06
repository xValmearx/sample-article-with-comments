from django.contrib import admin
from .models import Article, Comment


class CommentInLine(admin.StackedInline):
    """Comment InLine for Articles Admin"""

    # could sue admin.StackedInlIne as the class to inherit form
    # if we wanted a different looking inline that is "stacked" vs "horizontal"

    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    """Article Admin"""

    inlines = [CommentInLine]


# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
