from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from crushapp.models import Crush, calculate, count_char

def index(request):
	if request.method == 'POST':
		fname = request.POST['fname'].lower()
		lname = request.POST['lname'].lower()
		fullname = fname + 'loves' + lname
		result = count_char(fullname)
		final_result = calculate(result)
		a = Crush()
		a.first_name = fname
		a.crush_name = lname
		a.crush = int(final_result)
		a.save()
		return render_to_response('index.html', context_instance=RequestContext(request, {'data':final_result, 'fname':fname, 'lname':lname}))
	else:
		return render_to_response('index.html', context_instance=RequestContext(request))
