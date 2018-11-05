from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import models
import markdown

# Create your views here.
def index(request):
	articles = models.article.objects.order_by('pub_time').reverse()
	tags = set((article.tag for article in articles))
	few_texts = (article.content[:500] for article in articles)
	# 判断有没有置顶
	try:
		topArticle = models.article.objects.get(isTop=1)
	except Exception as e:
		return render(request, 'blog/index.html', {'zip': zip(articles, few_texts)})
	finally:
		return render(request, 'blog/index.html', {'zip': zip(articles, few_texts), 'topArticle':topArticle})

def article_page(request, article_id):
# article = models.article.objects.get(pk=article_id)
# return render(request, 'blog/article_page.html', {'article':article})
	article = get_object_or_404(models.article, pk=article_id)
	article.increase_views()
	article.content = markdown.markdown(article.content,
		extensions=[
		'markdown.extensions.extra',
		'markdown.extensions.codehilite',
		'markdown.extensions.toc',
		])
	return render(request, 'blog/article_page.html', context={'article': article})

def edit_action(request):
	title = request.POST.get('title', "TITLE")
	content = request.POST.get('content', "None")
	article_id = request.POST.get('article_id', '0')
	tag = request.POST.get('tag', 'None')

	if str(article_id) == '0':
		article = models.article.objects.create(title=title, content=content)
		article.save()
		return redirect('/article/' + str(article.id))

	else:
		article = models.article.objects.get(pk=article_id)
		article.title = title
		article.content = content
		article.tag = tag
		article.save()
		return redirect('/article/' + str(article.id))

def edit_page(request, article_id):
	if str(article_id) == '0':
		return render(request, 'blog/edit_page.html')
	else:
		article = models.article.objects.get(pk=article_id)
		return render(request, 'blog/edit_page.html', {'article':article})


def about(request):
	return render(request, 'blog/about.html')

def tag(request):
	articles = models.article.objects.all()
	tags = set((article.tag for article in articles))
	return render(request, 'blog/tag.html', {'tags': tags})

def tag_articles(request, tag):
	articles = models.article.objects.filter(tag=tag)
	few_texts = (article.content[:20] for article in articles)
	return render(request, 'blog/tag_articles.html', {'zip': zip(articles, few_texts)})