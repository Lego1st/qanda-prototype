# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from .models import Question, Choice
from django.template import loader

# Create your views here.
def index(request):
	lastest_questions = Question.objects.order_by('-pub_date')[:3]
	template = loader.get_template('polls/index.html')
	context = { 'latest_question_list' : lastest_questions, }
	return HttpResponse(template.render(context, request))

def home(request):
	template = loader.get_template('polls/home.html')
	top_users = ['user1', 'user2', 'user3']
	questions = [1, 2, 3, 4, 5]
	return HttpResponse(template.render(context = {'top_users' : top_users, 'questions' : questions}))
	
def detail(request, question_id):
	template = loader.get_template('polls/details.html')
	return HttpResponse(template.render(context = {'question_id': question_id}))

def results(request, question_id):
	return HttpResponse('The results of question %s' % question_id)

def vote(request, question_id):
	return HttpResponse('You are upvoting for question %s' % question_id)