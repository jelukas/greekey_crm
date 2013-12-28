from django.shortcuts import render_to_response, RequestContext


def base(request):
	response = {}
	return render_to_response('base.html',{},context_instance=RequestContext(request))