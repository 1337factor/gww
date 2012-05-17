import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from api import queue


@csrf_exempt
def index(request):
	# Just save into the provider
	queue.post_to_provider(request.raw_post_data)

	return HttpResponse(json.dumps({'status': 'ok'}))