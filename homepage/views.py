from django.http import HttpResponse
from django.template import RequestContext, loader
from homepage.models import Article

def index(request):
	article_list=Article.objects.order_by('id')[:5]

	template=loader.get_template('homepage/index.html')
	context=RequestContext(request, {
	        'article_list': article_list,
			})
    
    	return HttpResponse(template.render(context))