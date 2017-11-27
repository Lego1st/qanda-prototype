from django import forms

from .models import Question, Answer

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'content']
		labels = {'title' : 'Question:', 'content' : 'More description:'}
		widgets = {'title' : forms.TextInput(attrs={'size':80}), 'content': forms.Textarea(attrs={'cols': 80})}

class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ['content']
		labels = {'content' : ''}
		widgets = {'content' : forms.Textarea(attrs={'cols': 80})}