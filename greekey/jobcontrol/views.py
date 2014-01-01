from datetime import datetime
from django.utils.timezone import utc
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import GeneralTimerRegistry
from .utils import seconds_to_human_string


@login_required
def start_general_timer(request):
	if request.method == 'GET':
		timer = GeneralTimerRegistry()
		timer.start_working = datetime.utcnow().replace(tzinfo=utc)
		timer.worker = request.user
		timer.save()
		messages.success(request, 'Your General Time has Started.')
	else:
		messages.error(request, 'The Timer can\'t Start', extra_tags='danger')

	#Redirect to Previous Page or Main Page
	try:
		next_page = request.META['HTTP_REFERER']
	except KeyError:
		next_page = '/'
	return redirect(next_page)


@login_required
def stop_general_timer(request):
	if request.method == 'GET':
		timer = GeneralTimerRegistry.objects.get(end_working = None)
		timer.end_working = datetime.utcnow().replace(tzinfo=utc)
		timer.save()
		messages.success(request, 'General Timer Stoped.')
	else:
		messages.error(request, 'The Timer can\'t be Stopped', extra_tags='danger')

	#Redirect to Previous Page or Main Page
	try:
		next_page = request.META['HTTP_REFERER']
	except KeyError:
		next_page = '/'
	return redirect(next_page)


@login_required
def index(request):
	general_timer_active = GeneralTimerRegistry.objects.filter(worker = request.user,end_working = None).first()
	timers = GeneralTimerRegistry.objects.filter(worker = request.user)
	time_of_month = GeneralTimerRegistry.get_month_working_time_by_user(request.user, datetime.now().month, datetime.now().year)
	context = { 'general_timer_active': general_timer_active, 'timers': timers, 'time_of_month': time_of_month}
	return render(request, 'jobcontrol/index.html', context)