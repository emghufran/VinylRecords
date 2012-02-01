# Create your views here.
from django.template import RequestContext, loader
#from polls.models import Poll
from django.http import HttpResponse

def homepage(request):
	t = loader.get_template('vrec/homepage.html')
	c = RequestContext( request, { 
		'latest_poll_list': 'abcd', 
	})
	return HttpResponse(t.render(c))