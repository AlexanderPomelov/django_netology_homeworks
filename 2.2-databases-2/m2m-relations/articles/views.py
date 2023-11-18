from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'

    show_article = Article.objects.order_by(ordering).all()
    context = {'object_list': show_article}

    return render(request, template, context)
