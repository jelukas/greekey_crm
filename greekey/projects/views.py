from django.shortcuts import render_to_response, RequestContext, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm


@login_required
def index(request):
	context = {}
	return render_to_response('base.html', context, context_instance=RequestContext(request))


def add_project(request):
	context = {}
	if request.method == 'POST':
		project_form = ProjectForm(request.POST)
		if project_form.is_valid():
			project_form.save()
			return redirect('/')
	else:
		project_form = ProjectForm()
	context.update({'project_form': project_form})
	return render_to_response('projects/add_project.html', context, context_instance=RequestContext(request))
