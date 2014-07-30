from django.http import HttpResponse
from django.template import RequestContext, loader
from homepage.models import Article

def index(request):
	article_list=Article.objects.exclude(main_title='About Me')
	about_me=Article.objects.filter(main_title='About Me')

	template=loader.get_template('homepage/index.html')
	context=RequestContext(request, {
	        'article_list': article_list,
	        'about_me': about_me,
			})
    
    	return HttpResponse(template.render(context))