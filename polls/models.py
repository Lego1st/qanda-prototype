# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#Database for polls 

class Question(models.Model):
	title = models.CharField(max_length=200)
	content = models.CharField(max_length=1000)
	time = models.DateTimeField('date asked')
	# user = models.ForeignKey(User, on_delete=models.CASCADE)

class Answer(models.Model):
	content = models.CharField(max_length=1000)
	time = models.DateTimeField('date answered')
	accepted = models.BooleanField(default=False)
	# user = models.ForeignKey(User, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)

# class Reply(models.Model):
# 	time = models.DateTimeField('date replied')
# 	content = models.CharField(max_length=1000)
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

# class Follow(models.Model):
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	question = models.ForeignKey(Question, on_delete=models.CASCADE)

# class Vote(models.Model):
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

# class Category(models.Model):
# 	question = models.ForeignKey(Question, on_delete=modes.CASCADE)
		 

