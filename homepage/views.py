from django.http import HttpResponse
from django.template import RequestContext, loader
from homepage.models import Article
from homepage.helper.form_helper import ContactForm
from django.core.mail import send_mail

def index(request):
	article_list=Article.objects.exclude(main_title='About Me')
	about_me=Article.objects.filter(main_title='About Me')

	template=loader.get_template('homepage/index.html')
	context=RequestContext(request, {
		'article_list': article_list,
		'about_me': about_me,
		'menu': 'home',
	})
	return HttpResponse(template.render(context))

def contact(request):

	#form loader
	emailResult = ""

	if request.method == 'POST':

		contactForm = ContactForm(request.POST)

		if contactForm.is_valid():
		    subject = contactForm.cleaned_data['subject']
		    message = contactForm.cleaned_data['message']
		    sender = contactForm.cleaned_data['sender']
		    recipients = ['lcxfs1991@gmail.com']

		    if send_mail(subject, message, sender, recipients, fail_silently=False):
		    	emailResult = "Your message has been successfully sent to me! Thank you!"
		    else:
		    	emailResult = "Your message fails to be sent!"

		else:
			emailResult = "Your submit information has not been completed"
	else:
		contactForm = ContactForm()

	#template loader
	template=loader.get_template('homepage/contact.html')
	context=RequestContext(request, {
		'menu': 'contact',
		'contactForm': contactForm,
		'emailResult': emailResult,
	})

	return HttpResponse(template.render(context))