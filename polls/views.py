# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, Http404
from django.template import loader
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import UpdateView
from django.utils import timezone

from .models import Question
from .forms import QuestionForm
# Create your views here.
def index(request):
	lastest_questions = Question.objects.order_by('-pub_date')[:3]
	template = loader.get_template('polls/index.html')
	context = { 'latest_question_list' : lastest_questions, }
	return HttpResponse(template.render(context, request))

def home(request):
	""" Render a homepage """
	template = loader.get_template('polls/home.html')
	top_users = ['user1', 'user2', 'user3']
	# questions = [1, 2, 3, 4, 5]
	questions = Question.objects.order_by('-time')[:3]
	return HttpResponse(template.render(context = {'top_users' : top_users, 'questions' : questions}))

def new_question(request):
	"""Add a new question. """
	if request.method != 'POST':
		# No data. Create a blank form
		form = QuestionForm()
	else:
		# Data submitted; process data
		form = QuestionForm(request.POST)
		if form.is_valid():
			new_ques = form.save(commit=False)
			new_ques.time = timezone.now()
			new_ques.save()
			return HttpResponseRedirect(reverse('polls:home'))
	context = {'form': form}
	return render(request, 'polls/new_question.html', context)

def detail(request, question_id):
	template = loader.get_template('polls/details.html')
	try:
		question = Question.objects.get(id=question_id)
	except:
		raise Http404("Question does not exist")
	return HttpResponse(template.render(context = {'question': question}))

def results(request, question_id):
	return HttpResponse('The results of question %s' % question_id)

def vote(request, question_id):
	return HttpResponse('You are upvoting for question %s' % question_id)