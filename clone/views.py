from django.shortcuts import render_to_response, get_object_or_404

from models import Forum
# Create your views here.
def index(request):
	return render_to_response('index.html'{
		'Title':Title.objects.all(),
		'Link':Link.objects.all(),
		'Votes':Link.objects.all(),
		'Time':Link.objects.all(),
		'Comments': Comment.objects.all(),
	})

